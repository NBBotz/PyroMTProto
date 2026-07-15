#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram
from pyrogram import raw, utils
from pyrogram import types
from pyrogram.file_id import FileId, FileType, FileUniqueId, FileUniqueType
from ..object import Object


class VideoNote(Object):
    """A video note.

    Parameters:
        file_id (``str``):
            Identifier for this file, which can be used to download or reuse the file.

        file_unique_id (``str``):
            Unique identifier for this file, which is supposed to be the same over time and for different accounts.
            Can't be used to download or reuse the file.

        length (``int``):
            Video width and height as defined by sender.

        duration (``int``):
            Duration of the video in seconds as defined by sender.

        mime_type (``str``, *optional*):
            MIME type of the file as defined by sender.

        file_size (``int``, *optional*):
            File size.

        date (:py:obj:`~datetime.datetime`, *optional*):
            Date the video note was sent.

        ttl_seconds (``int``, *optional*):
            Time-to-live seconds, for one-time media.

        thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
            Video thumbnails.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        thumbs: list["types.Thumbnail"] = None,
        mime_type: str = None,
        file_size: int = None,
        date: datetime = None,
        ttl_seconds: int = None
    ):
        super().__init__(client)

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.mime_type = mime_type
        self.file_size = file_size
        self.date = date
        self.ttl_seconds = ttl_seconds
        self.length = length
        self.duration = duration
        self.thumbs = thumbs

    @staticmethod
    def _parse(
        client,
        video_note: "raw.types.Document",
        video_attributes: "raw.types.DocumentAttributeVideo",
        ttl_seconds: int = None
    ) -> "VideoNote":
        return VideoNote(
            file_id=FileId(
                file_type=FileType.VIDEO_NOTE,
                dc_id=video_note.dc_id,
                media_id=video_note.id,
                access_hash=video_note.access_hash,
                file_reference=video_note.file_reference
            ).encode() if video_note else None,
            file_unique_id=FileUniqueId(
                file_unique_type=FileUniqueType.DOCUMENT,
                media_id=video_note.id
            ).encode() if video_note else None,
            length=video_attributes.w if video_attributes else None,
            duration=video_attributes.duration if video_attributes else None,
            file_size=video_note.size if video_note else None,
            mime_type=video_note.mime_type if video_note else None,
            date=utils.timestamp_to_datetime(video_note.date) if video_note else None,
            ttl_seconds=ttl_seconds,
            thumbs=types.Thumbnail._parse(client, video_note) if video_note else None,
            client=client
        )
