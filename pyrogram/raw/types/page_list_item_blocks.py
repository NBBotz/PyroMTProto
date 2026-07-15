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


class PageListItemBlocks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageListItem`.

    Details:
        - Layer: ``227``
        - ID: ``63CA67AA``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        checkbox (``bool``, *optional*):
            N/A

        checked (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "checkbox", "checked"]

    ID = 0x63ca67aa
    QUALNAME = "types.PageListItemBlocks"

    def __init__(self, *, blocks: list["raw.base.PageBlock"], checkbox: Optional[bool] = None, checked: Optional[bool] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.checkbox = checkbox  # flags.0?true
        self.checked = checked  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListItemBlocks":
        
        flags = Int.read(b)
        
        checkbox = True if flags & (1 << 0) else False
        checked = True if flags & (1 << 1) else False
        blocks = TLObject.read(b)
        
        return PageListItemBlocks(blocks=blocks, checkbox=checkbox, checked=checked)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.checkbox else 0
        flags |= (1 << 1) if self.checked else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        return b.getvalue()
