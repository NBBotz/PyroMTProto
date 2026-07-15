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


class RequestedPeerChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RequestedPeer`.

    Details:
        - Layer: ``227``
        - ID: ``7307544F``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["chat_id", "title", "photo"]

    ID = 0x7307544f
    QUALNAME = "types.RequestedPeerChat"

    def __init__(self, *, chat_id: int, title: Optional[str] = None, photo: "raw.base.Photo" = None) -> None:
        self.chat_id = chat_id  # long
        self.title = title  # flags.0?string
        self.photo = photo  # flags.2?Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerChat":
        
        flags = Int.read(b)
        
        chat_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        photo = TLObject.read(b) if flags & (1 << 2) else None
        
        return RequestedPeerChat(chat_id=chat_id, title=title, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 2) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.chat_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()
