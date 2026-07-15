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


class StarsSubscriptionPricing(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsSubscriptionPricing`.

    Details:
        - Layer: ``227``
        - ID: ``5416D58``

    Parameters:
        period (``int`` ``32-bit``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["period", "amount"]

    ID = 0x5416d58
    QUALNAME = "types.StarsSubscriptionPricing"

    def __init__(self, *, period: int, amount: int) -> None:
        self.period = period  # int
        self.amount = amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsSubscriptionPricing":
        # No flags
        
        period = Int.read(b)
        
        amount = Long.read(b)
        
        return StarsSubscriptionPricing(period=period, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.period))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
