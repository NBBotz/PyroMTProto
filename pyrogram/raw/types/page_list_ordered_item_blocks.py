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


class PageListOrderedItemBlocks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageListOrderedItem`.

    Details:
        - Layer: ``227``
        - ID: ``8FF2D5F0``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        checkbox (``bool``, *optional*):
            N/A

        checked (``bool``, *optional*):
            N/A

        num (``str``, *optional*):
            N/A

        value (``int`` ``32-bit``, *optional*):
            N/A

        type (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "checkbox", "checked", "num", "value", "type"]

    ID = 0x8ff2d5f0
    QUALNAME = "types.PageListOrderedItemBlocks"

    def __init__(self, *, blocks: list["raw.base.PageBlock"], checkbox: Optional[bool] = None, checked: Optional[bool] = None, num: Optional[str] = None, value: Optional[int] = None, type: Optional[str] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.checkbox = checkbox  # flags.0?true
        self.checked = checked  # flags.1?true
        self.num = num  # flags.2?string
        self.value = value  # flags.3?int
        self.type = type  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListOrderedItemBlocks":
        
        flags = Int.read(b)
        
        checkbox = True if flags & (1 << 0) else False
        checked = True if flags & (1 << 1) else False
        num = String.read(b) if flags & (1 << 2) else None
        blocks = TLObject.read(b)
        
        value = Int.read(b) if flags & (1 << 3) else None
        type = String.read(b) if flags & (1 << 4) else None
        return PageListOrderedItemBlocks(blocks=blocks, checkbox=checkbox, checked=checked, num=num, value=value, type=type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.checkbox else 0
        flags |= (1 << 1) if self.checked else 0
        flags |= (1 << 2) if self.num is not None else 0
        flags |= (1 << 3) if self.value is not None else 0
        flags |= (1 << 4) if self.type is not None else 0
        b.write(Int(flags))
        
        if self.num is not None:
            b.write(String(self.num))
        
        b.write(Vector(self.blocks))
        
        if self.value is not None:
            b.write(Int(self.value))
        
        if self.type is not None:
            b.write(String(self.type))
        
        return b.getvalue()
