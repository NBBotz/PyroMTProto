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


class PageBlockBlockquoteBlocks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``227``
        - ID: ``E6E47C4``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        caption (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

    """

    __slots__: list[str] = ["blocks", "caption"]

    ID = 0xe6e47c4
    QUALNAME = "types.PageBlockBlockquoteBlocks"

    def __init__(self, *, blocks: list["raw.base.PageBlock"], caption: "raw.base.RichText") -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockBlockquoteBlocks":
        # No flags
        
        blocks = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockBlockquoteBlocks(blocks=blocks, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.blocks))
        
        b.write(self.caption.write())
        
        return b.getvalue()
