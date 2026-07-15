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


class StarGiftAttributeRarity(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttributeRarity`.

    Details:
        - Layer: ``227``
        - ID: ``36437737``

    Parameters:
        permille (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["permille"]

    ID = 0x36437737
    QUALNAME = "types.StarGiftAttributeRarity"

    def __init__(self, *, permille: int) -> None:
        self.permille = permille  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeRarity":
        # No flags
        
        permille = Int.read(b)
        
        return StarGiftAttributeRarity(permille=permille)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.permille))
        
        return b.getvalue()
