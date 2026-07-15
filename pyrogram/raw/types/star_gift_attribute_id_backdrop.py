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


class StarGiftAttributeIdBackdrop(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttributeId`.

    Details:
        - Layer: ``227``
        - ID: ``1F01C757``

    Parameters:
        backdrop_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["backdrop_id"]

    ID = 0x1f01c757
    QUALNAME = "types.StarGiftAttributeIdBackdrop"

    def __init__(self, *, backdrop_id: int) -> None:
        self.backdrop_id = backdrop_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeIdBackdrop":
        # No flags
        
        backdrop_id = Int.read(b)
        
        return StarGiftAttributeIdBackdrop(backdrop_id=backdrop_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.backdrop_id))
        
        return b.getvalue()
