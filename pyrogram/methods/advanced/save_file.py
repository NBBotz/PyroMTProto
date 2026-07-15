#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0
#
#  Upload engine: parallel pool + read-ahead + per-worker retry
#  Target: 20–30 MB/s on free accounts

import asyncio
import functools
import inspect
import io
import logging
import math
import os
import time
from hashlib import md5
from pathlib import PurePath
from typing import Union, BinaryIO, Callable, Optional

import pyrogram
from pyrogram import StopTransmission, raw

log = logging.getLogger(__name__)

PART_SIZE          = 512 * 1024   # Telegram hard ceiling per part
WORKERS_PER_SESSION = 4           # concurrent parts per session
POOL_SIZE          = 4            # parallel sessions for big files
MAX_RETRIES        = 5
READ_BUFFER        = 4 * 1024 * 1024   # 4 MB read buffer
PROGRESS_INTERVAL  = 0.1          # seconds between progress callbacks


def _pool_params(file_size: int, is_premium: bool) -> tuple[int, int]:
    """Return (pool_size, workers_per_session) based on file size."""
    if file_size < 5 * 1024 * 1024:
        return 1, 2
    elif file_size < 25 * 1024 * 1024:
        return 2, 4
    elif file_size < 100 * 1024 * 1024:
        return 4, 4
    else:
        return (6 if is_premium else 4), 4


class SaveFile:
    async def save_file(
        self: "pyrogram.Client",
        path: Union[str, BinaryIO],
        file_id: Optional[int] = None,
        file_part: int = 0,
        progress: Optional[Callable] = None,
        progress_args: tuple = (),
    ):
        """Upload a file to Telegram servers.

        Uses a parallel pool of sessions with read-ahead buffering for
        maximum throughput (20–30 MB/s on free accounts).
        """
        async with self.save_file_semaphore:
            if path is None:
                return None

            # ── worker: pulls RPCs from queue, retries on transient errors ──
            async def worker(session):
                while True:
                    data = await queue.get()
                    if data is None:
                        return
                    for attempt in range(MAX_RETRIES):
                        try:
                            await session.invoke(data)
                            break
                        except StopTransmission:
                            raise
                        except pyrogram.errors.FloodWait as e:
                            wait = e.value
                            log.warning(f"FloodWait {wait}s in upload worker")
                            await asyncio.sleep(wait)
                        except Exception as e:
                            if attempt == MAX_RETRIES - 1:
                                log.error(f"Upload part failed after {MAX_RETRIES} attempts: {e}")
                                raise
                            log.warning(f"Upload retry {attempt + 1}/{MAX_RETRIES}: {e}")
                            await asyncio.sleep(2 ** attempt)

            # ── async read-ahead: overlaps disk I/O with network ──
            async def read_chunk():
                return await self.loop.run_in_executor(
                    self.executor, fp.read, PART_SIZE
                )

            # ── open file ─────────────────────────────────────────────────
            if isinstance(path, (str, PurePath)):
                fp = open(path, "rb", buffering=READ_BUFFER)
                must_close = True
            elif isinstance(path, io.IOBase):
                fp = path
                must_close = False
            else:
                raise ValueError("Invalid file — expected path string or binary file object")

            file_name = getattr(fp, "name", "file.bin")

            fp.seek(0, os.SEEK_END)
            file_size = fp.tell()
            fp.seek(0)

            if file_size == 0:
                raise ValueError("File size is 0 bytes")

            is_premium = bool(getattr(self.me, "is_premium", False)) if self.me else False
            file_size_limit_mib = 4000 if is_premium else 2000
            if file_size > file_size_limit_mib * 1024 * 1024:
                raise ValueError(f"Can't upload files bigger than {file_size_limit_mib} MiB")

            file_total_parts = math.ceil(file_size / PART_SIZE)
            is_big = file_size > 10 * 1024 * 1024
            is_missing_part = file_id is not None
            file_id = file_id or self.rnd_id()
            md5_sum = md5() if not is_big and not is_missing_part else None

            pool_size, workers_per_session = _pool_params(file_size, is_premium)
            if not is_big:
                pool_size, workers_per_session = 1, 1

            # ── build session pool ─────────────────────────────────────────
            dc_id = await self.storage.dc_id()
            pool = await self._get_media_session_pool(dc_id, pool_size)

            n_sessions = len(pool)
            n_workers  = n_sessions * workers_per_session
            queue      = asyncio.Queue(n_workers)
            workers    = [
                self.loop.create_task(worker(pool[i % n_sessions]))
                for i in range(n_workers)
            ]

            next_chunk_task = None
            _last_progress  = 0.0

            try:
                fp.seek(PART_SIZE * file_part)
                # kick off first read-ahead
                next_chunk_task = self.loop.create_task(read_chunk())

                while True:
                    chunk = await next_chunk_task
                    # start reading next chunk while we enqueue this one
                    next_chunk_task = self.loop.create_task(read_chunk())

                    if not chunk:
                        next_chunk_task.cancel()
                        if not is_big and not is_missing_part:
                            md5_sum = md5_sum.hexdigest()
                        break

                    # check if any worker died
                    if all(t.done() for t in workers):
                        for t in workers:
                            if t.exception():
                                raise t.exception()
                        raise RuntimeError("All upload workers exited unexpectedly")

                    # build RPC for this part
                    if is_big:
                        rpc = raw.functions.upload.SaveBigFilePart(
                            file_id=file_id,
                            file_part=file_part,
                            file_total_parts=file_total_parts,
                            bytes=chunk,
                        )
                    else:
                        rpc = raw.functions.upload.SaveFilePart(
                            file_id=file_id,
                            file_part=file_part,
                            bytes=chunk,
                        )

                    await queue.put(rpc)

                    # resume interrupted upload
                    if is_missing_part:
                        next_chunk_task.cancel()
                        for _ in range(n_workers):
                            await queue.put(None)
                        results = await asyncio.gather(*workers, return_exceptions=True)
                        for r in results:
                            if isinstance(r, BaseException) and not isinstance(r, asyncio.CancelledError):
                                raise r
                        return None

                    if not is_big and not is_missing_part and md5_sum:
                        md5_sum.update(chunk)

                    file_part += 1

                    # progress callback (rate-limited)
                    if progress:
                        now = time.monotonic()
                        if now - _last_progress >= PROGRESS_INTERVAL:
                            _last_progress = now
                            sent  = min(file_part * PART_SIZE, file_size)
                            total = file_size

                            async def _report(s=sent, t=total):
                                try:
                                    if inspect.iscoroutinefunction(progress):
                                        await progress(s, t, *progress_args)
                                    else:
                                        await self.loop.run_in_executor(
                                            self.executor,
                                            functools.partial(progress, s, t, *progress_args)
                                        )
                                except Exception as e:
                                    log.warning(f"Progress callback error: {e}")

                            asyncio.ensure_future(_report())

            except StopTransmission:
                raise
            except Exception as e:
                log.exception(e)
                raise
            else:
                if is_big:
                    return raw.types.InputFileBig(
                        id=file_id,
                        parts=file_total_parts,
                        name=file_name,
                    )
                else:
                    return raw.types.InputFile(
                        id=file_id,
                        parts=file_total_parts,
                        name=file_name,
                        md5_checksum=md5_sum,
                    )
            finally:
                if next_chunk_task and not next_chunk_task.done():
                    next_chunk_task.cancel()
                for _ in workers:
                    await queue.put(None)
                await asyncio.gather(*workers, return_exceptions=True)
                if must_close:
                    fp.close()
