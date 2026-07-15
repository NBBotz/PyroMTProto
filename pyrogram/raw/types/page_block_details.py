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


class PageBlockDetails(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``227``
        - ID: ``76768BED``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        title (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        open (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "title", "open"]

    ID = 0x76768bed
    QUALNAME = "types.PageBlockDetails"

    def __init__(self, *, blocks: list["raw.base.PageBlock"], title: "raw.base.RichText", open: Optional[bool] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.title = title  # RichText
        self.open = open  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockDetails":
        
        flags = Int.read(b)
        
        open = True if flags & (1 << 0) else False
        blocks = TLObject.read(b)
        
        title = TLObject.read(b)
        
        return PageBlockDetails(blocks=blocks, title=title, open=open)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        b.write(self.title.write())
        
        return b.getvalue()
