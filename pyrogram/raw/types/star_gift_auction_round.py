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


class StarGiftAuctionRound(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAuctionRound`.

    Details:
        - Layer: ``227``
        - ID: ``3AAE0528``

    Parameters:
        num (``int`` ``32-bit``):
            N/A

        duration (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["num", "duration"]

    ID = 0x3aae0528
    QUALNAME = "types.StarGiftAuctionRound"

    def __init__(self, *, num: int, duration: int) -> None:
        self.num = num  # int
        self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionRound":
        # No flags
        
        num = Int.read(b)
        
        duration = Int.read(b)
        
        return StarGiftAuctionRound(num=num, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.num))
        
        b.write(Int(self.duration))
        
        return b.getvalue()
