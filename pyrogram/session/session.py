#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import asyncio
import bisect
import logging
import os
from collections import deque
from hashlib import sha1
from io import BytesIO

import pyrogram
from pyrogram import raw
from pyrogram.connection import Connection
from pyrogram.crypto import mtproto
from pyrogram.errors import (
    RPCError, InternalServerError, AuthKeyDuplicated,
    FloodWait, FloodPremiumWait,
    ServiceUnavailable, BadMsgNotification,
    SecurityCheckMismatch,
)
from pyrogram.raw.all import layer
from pyrogram.raw.core import TLObject, MsgContainer, Int, FutureSalts
from .internals import MsgId, MsgFactory

log = logging.getLogger(__name__)


class Result:
    __slots__ = ("value", "event")

    def __init__(self):
        self.value = None
        self.event = asyncio.Event()


class Session:
    START_TIMEOUT = 2
    WAIT_TIMEOUT = 15
    SLEEP_THRESHOLD = 10
    MAX_RETRIES = 5
    ACKS_THRESHOLD = 8
    PING_INTERVAL = 5
    # Use deque maxlen instead of bounded list for O(1) append/discard
    STORED_MSG_IDS_MAX_SIZE = 2000

    TRANSPORT_ERRORS = {
        404: "auth key not found",
        429: "transport flood",
        444: "invalid DC"
    }

    CUR_ALWD_INNR_QRYS = (
        raw.functions.InvokeWithoutUpdates,
        raw.functions.InvokeWithTakeout,
        raw.functions.InvokeWithBusinessConnection,
    )

    def __init__(
        self,
        client: "pyrogram.Client",
        dc_id: int,
        auth_key: bytes,
        test_mode: bool,
        is_media: bool = False,
        is_cdn: bool = False
    ):
        self.client = client
        self.dc_id = dc_id
        self.auth_key = auth_key
        self.test_mode = test_mode
        self.is_media = is_media
        self.is_cdn = is_cdn

        self.connection: Connection | None = None

        self.auth_key_id = sha1(auth_key).digest()[-8:]

        self.session_id = os.urandom(8)
        self.msg_factory = MsgFactory()

        self.salt = 0

        self.pending_acks: set = set()

        self.results: dict = {}

        # O(1) bounded deque for message ID deduplication (replaces O(n) list pop)
        self.stored_msg_ids: deque[int] = deque(maxlen=self.STORED_MSG_IDS_MAX_SIZE)
        # Keep sorted list in sync for bisect lookups
        self._stored_msg_ids_sorted: list[int] = []

        self.ping_task = None
        self.recv_task = None
        self.is_connected = asyncio.Event()

    def _store_msg_id(self, msg_id: int) -> bool:
        """Store a message ID for deduplication. Returns True if it's new."""
        # Check duplicate using sorted list + bisect: O(log n)
        pos = bisect.bisect_left(self._stored_msg_ids_sorted, msg_id)
        if pos < len(self._stored_msg_ids_sorted) and self._stored_msg_ids_sorted[pos] == msg_id:
            return False  # duplicate

        # Evict oldest if at capacity before inserting
        if len(self.stored_msg_ids) == self.STORED_MSG_IDS_MAX_SIZE:
            oldest = self.stored_msg_ids[0]  # deque[0] is O(1)
            old_pos = bisect.bisect_left(self._stored_msg_ids_sorted, oldest)
            if old_pos < len(self._stored_msg_ids_sorted) and self._stored_msg_ids_sorted[old_pos] == oldest:
                self._stored_msg_ids_sorted.pop(old_pos)

        self.stored_msg_ids.append(msg_id)
        bisect.insort(self._stored_msg_ids_sorted, msg_id)
        return True

    async def start(self):
        while True:
            self.connection = Connection(
                self.dc_id,
                self.test_mode,
                self.client.ipv6,
                self.client.proxy,
                self.is_media,
                self.client.connection_mode,
            )

            try:
                await self.connection.connect()

                self.recv_task = asyncio.get_event_loop().create_task(self.recv_worker())

                await self.send(raw.functions.Ping(ping_id=0), timeout=self.START_TIMEOUT)

                if not self.is_cdn:
                    await self.send(
                        raw.functions.InvokeWithLayer(
                            layer=layer,
                            query=raw.functions.InitConnection(
                                api_id=await self.client.storage.api_id(),
                                app_version=self.client.app_version,
                                device_model=self.client.device_model,
                                lang_code=self.client.lang_code,
                                lang_pack=self.client.lang_pack,
                                system_lang_code=self.client.system_lang_code,
                                system_version=self.client.system_version,
                                query=raw.functions.help.GetConfig(),
                                params=None,
                            )
                        ),
                        timeout=self.START_TIMEOUT
                    )

                self.ping_task = asyncio.get_event_loop().create_task(self.ping_worker())
                self.is_connected.set()

                log.info(f"Session initialized: Layer {layer}")
                break
            except AuthKeyDuplicated as e:
                await self.stop()
                raise
            except (OSError, asyncio.TimeoutError, RPCError):
                await self.stop()
            except Exception as e:
                await self.stop()
                raise

    async def stop(self):
        self.is_connected.clear()

        if self.ping_task:
            self.ping_task.cancel()
            self.ping_task = None

        if self.recv_task:
            self.recv_task.cancel()
            self.recv_task = None

        if self.connection:
            self.connection.close()
            self.connection = None

        for result in self.results.values():
            result.event.set()

        self.results.clear()

    async def restart(self):
        await self.stop()
        await self.start()

    async def send(self, data: TLObject, retries: int = MAX_RETRIES, timeout: float = WAIT_TIMEOUT, sleep_threshold: float = SLEEP_THRESHOLD):
        is_function = isinstance(data, raw.functions)

        for attempt in range(retries + 1):
            msg = self.msg_factory(data)
            msg_id = msg.msg_id

            if is_function:
                self.results[msg_id] = Result()

            try:
                payload = await asyncio.get_event_loop().run_in_executor(
                    pyrogram.crypto_executor,
                    mtproto.pack,
                    msg,
                    self.salt,
                    self.session_id,
                    self.auth_key,
                    self.auth_key_id
                )

                await self.connection.send(payload)

                if is_function:
                    r = self.results[msg_id]

                    try:
                        await asyncio.wait_for(r.event.wait(), timeout)
                    except asyncio.TimeoutError:
                        raise TimeoutError(f"Request timed out after {timeout}s: {data}")

                    if r.value is None:
                        raise ConnectionError("Session closed while waiting for response")

                    if isinstance(r.value, RPCError):
                        if isinstance(r.value, FloodWait | FloodPremiumWait):
                            wait = r.value.value

                            if wait > sleep_threshold:
                                raise r.value

                            log.warning(f"Sleeping for {wait}s (FloodWait)")
                            await asyncio.sleep(wait)
                            continue
                        else:
                            raise r.value

                    return r.value
                else:
                    return
            except asyncio.TimeoutError:
                if attempt < retries:
                    log.warning(f"Request timeout, attempt {attempt + 1}/{retries}")
                    await asyncio.sleep(0.5)
                    continue
                raise
            except (FloodWait, FloodPremiumWait):
                raise
            except RPCError:
                raise
            except (ConnectionError, OSError) as e:
                if attempt < retries:
                    log.warning(f"Connection error: {e}, reconnecting...")
                    await self.restart()
                    continue
                raise
            finally:
                if is_function and msg_id in self.results:
                    del self.results[msg_id]

    async def invoke(
        self,
        query: TLObject,
        retries: int = MAX_RETRIES,
        timeout: float = WAIT_TIMEOUT,
        sleep_threshold: float = SLEEP_THRESHOLD
    ):
        """Public invoke method - wraps queries that need InvokeWithoutUpdates for inner sessions."""
        available_functions = isinstance(query, self.CUR_ALWD_INNR_QRYS)

        if not available_functions and self.client.takeout_id:
            query = raw.functions.InvokeWithTakeout(
                takeout_id=self.client.takeout_id,
                query=query
            )

        return await self.send(query, retries=retries, timeout=timeout, sleep_threshold=sleep_threshold)

    async def recv_worker(self):
        log.info("RecvTask started")

        while True:
            packet = await self.connection.recv()

            if packet is None or len(packet) < 4:
                if self.is_connected.is_set():
                    asyncio.get_event_loop().create_task(self.restart())
                break

            try:
                data = await asyncio.get_event_loop().run_in_executor(
                    pyrogram.crypto_executor,
                    mtproto.unpack,
                    BytesIO(packet),
                    self.session_id,
                    self.auth_key,
                    self.auth_key_id
                )

                messages = (
                    data.body.messages
                    if isinstance(data.body, MsgContainer)
                    else [data]
                )

                log.debug(f"Received {len(messages)} message(s)")

                for msg in messages:
                    if msg.seq_no % 2 != 0:
                        if not self._store_msg_id(msg.msg_id):
                            continue
                        self.pending_acks.add(msg.msg_id)

                    if isinstance(msg.body, (raw.types.MsgDetailedInfo, raw.types.MsgNewDetailedInfo)):
                        self.pending_acks.add(msg.body.answer_msg_id)
                        continue

                    if isinstance(msg.body, raw.types.NewSessionCreated):
                        continue

                    msg_id = None

                    if isinstance(msg.body, (raw.core.BadMsgNotification, raw.core.BadServerSalt)):
                        msg_id = msg.body.bad_msg_id
                    elif isinstance(msg.body, (FutureSalts, raw.types.RpcResult)):
                        msg_id = msg.body.req_msg_id
                    elif isinstance(msg.body, raw.types.Pong):
                        msg_id = msg.body.msg_id
                    else:
                        await self.client.handle_updates(msg.body)

                    if msg_id in self.results:
                        result = self.results[msg_id]

                        if isinstance(msg.body, raw.core.BadMsgNotification):
                            result.value = BadMsgNotification(msg.body.error_code)
                        elif isinstance(msg.body, raw.core.BadServerSalt):
                            self.salt = msg.body.new_server_salt
                            result.value = await self.send(self.results[msg_id])
                        elif isinstance(msg.body, raw.types.RpcResult):
                            body = msg.body.result
                            if isinstance(body, raw.types.RpcError):
                                result.value = RPCError.raise_it(body.error_code, body.error_message, query=None)
                            else:
                                result.value = body
                        elif isinstance(msg.body, FutureSalts):
                            result.value = msg.body
                        elif isinstance(msg.body, raw.types.Pong):
                            result.value = msg.body

                        result.event.set()

                if len(self.pending_acks) >= self.ACKS_THRESHOLD:
                    log.debug("Sending pending ACKs")
                    asyncio.get_event_loop().create_task(
                        self.send(raw.types.MsgsAck(msg_ids=list(self.pending_acks)))
                    )
                    self.pending_acks.clear()

            except SecurityCheckMismatch as e:
                log.info(f"Discarding packet: {e}")
                await self.stop()
                await self.restart()
                break
            except (asyncio.CancelledError, asyncio.TimeoutError):
                break
            except Exception as e:
                log.exception(f"recv_worker error: {e}")

        log.info("RecvTask stopped")

    async def ping_worker(self):
        log.info("PingTask started")

        while True:
            try:
                await asyncio.sleep(self.PING_INTERVAL)
                await self.send(
                    raw.functions.PingDelayDisconnect(
                        ping_id=0,
                        disconnect_delay=self.WAIT_TIMEOUT + 10
                    ),
                    timeout=self.PING_INTERVAL
                )
            except asyncio.CancelledError:
                break
            except OSError:
                break
            except Exception as e:
                log.warning(f"PingTask error: {e}")

        log.info("PingTask stopped")
