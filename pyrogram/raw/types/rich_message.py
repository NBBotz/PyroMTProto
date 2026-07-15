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


class RichMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RichMessage`.

    Details:
        - Layer: ``227``
        - ID: ``BAF39D8B``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        photos (List of :obj:`Photo <pyrogram.raw.base.Photo>`):
            N/A

        documents (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        rtl (``bool``, *optional*):
            N/A

        part (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "photos", "documents", "rtl", "part"]

    ID = 0xbaf39d8b
    QUALNAME = "types.RichMessage"

    def __init__(self, *, blocks: list["raw.base.PageBlock"], photos: list["raw.base.Photo"], documents: list["raw.base.Document"], rtl: Optional[bool] = None, part: Optional[bool] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.photos = photos  # Vector<Photo>
        self.documents = documents  # Vector<Document>
        self.rtl = rtl  # flags.0?true
        self.part = part  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RichMessage":
        
        flags = Int.read(b)
        
        rtl = True if flags & (1 << 0) else False
        part = True if flags & (1 << 1) else False
        blocks = TLObject.read(b)
        
        photos = TLObject.read(b)
        
        documents = TLObject.read(b)
        
        return RichMessage(blocks=blocks, photos=photos, documents=documents, rtl=rtl, part=part)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rtl else 0
        flags |= (1 << 1) if self.part else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
