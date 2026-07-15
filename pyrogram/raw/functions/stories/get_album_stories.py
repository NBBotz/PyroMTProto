#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from io import BytesIO
from typing import TYPE_CHECKING, Optional, Any

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject

if TYPE_CHECKING:
    from pyrogram import raw

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetAlbumStories(TLObject["raw.base.stories.Stories"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``AC806D61``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        album_id (``int`` ``32-bit``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`stories.Stories <pyrogram.raw.base.stories.Stories>`
    """

    __slots__: list[str] = ["peer", "album_id", "offset", "limit"]

    ID = 0xac806d61
    QUALNAME = "functions.stories.GetAlbumStories"

    def __init__(self, *, peer: "raw.base.InputPeer", album_id: int, offset: int, limit: int) -> None:
        self.peer = peer  # InputPeer
        self.album_id = album_id  # int
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAlbumStories":
        # No flags
        
        peer = TLObject.read(b)
        
        album_id = Int.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetAlbumStories(peer=peer, album_id=album_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.album_id))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
