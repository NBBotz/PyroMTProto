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


class StarGiftBackground(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftBackground`.

    Details:
        - Layer: ``227``
        - ID: ``AFF56398``

    Parameters:
        center_color (``int`` ``32-bit``):
            N/A

        edge_color (``int`` ``32-bit``):
            N/A

        text_color (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["center_color", "edge_color", "text_color"]

    ID = 0xaff56398
    QUALNAME = "types.StarGiftBackground"

    def __init__(self, *, center_color: int, edge_color: int, text_color: int) -> None:
        self.center_color = center_color  # int
        self.edge_color = edge_color  # int
        self.text_color = text_color  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftBackground":
        # No flags
        
        center_color = Int.read(b)
        
        edge_color = Int.read(b)
        
        text_color = Int.read(b)
        
        return StarGiftBackground(center_color=center_color, edge_color=edge_color, text_color=text_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.center_color))
        
        b.write(Int(self.edge_color))
        
        b.write(Int(self.text_color))
        
        return b.getvalue()
