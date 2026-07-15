#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw
from ..object import Object


class RtmpUrl(Object):
    """Represents an RTMP URL and stream key to be used in streaming software.

    Parameters:
        url (``str``):
            The URL.

        stream_key (``str``):
            Stream key.

    """

    def __init__(self, *, url: str, stream_key: str):
        super().__init__(None)

        self.url = url
        self.stream_key = stream_key

    @staticmethod
    def _parse(rtmp_url: "raw.types.GroupCallStreamRtmpUrl") -> "RtmpUrl":
        return RtmpUrl(
            url=rtmp_url.url,
            stream_key=rtmp_url.key
        )
