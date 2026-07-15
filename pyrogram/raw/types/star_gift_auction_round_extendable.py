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


class StarGiftAuctionRoundExtendable(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAuctionRound`.

    Details:
        - Layer: ``227``
        - ID: ``AA021E5``

    Parameters:
        num (``int`` ``32-bit``):
            N/A

        duration (``int`` ``32-bit``):
            N/A

        extend_top (``int`` ``32-bit``):
            N/A

        extend_window (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["num", "duration", "extend_top", "extend_window"]

    ID = 0xaa021e5
    QUALNAME = "types.StarGiftAuctionRoundExtendable"

    def __init__(self, *, num: int, duration: int, extend_top: int, extend_window: int) -> None:
        self.num = num  # int
        self.duration = duration  # int
        self.extend_top = extend_top  # int
        self.extend_window = extend_window  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionRoundExtendable":
        # No flags
        
        num = Int.read(b)
        
        duration = Int.read(b)
        
        extend_top = Int.read(b)
        
        extend_window = Int.read(b)
        
        return StarGiftAuctionRoundExtendable(num=num, duration=duration, extend_top=extend_top, extend_window=extend_window)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.num))
        
        b.write(Int(self.duration))
        
        b.write(Int(self.extend_top))
        
        b.write(Int(self.extend_window))
        
        return b.getvalue()
