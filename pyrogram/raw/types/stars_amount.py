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


class StarsAmount(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsAmount`.

    Details:
        - Layer: ``227``
        - ID: ``BBB6B4A3``

    Parameters:
        amount (``int`` ``64-bit``):
            N/A

        nanos (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["amount", "nanos"]

    ID = 0xbbb6b4a3
    QUALNAME = "types.StarsAmount"

    def __init__(self, *, amount: int, nanos: int) -> None:
        self.amount = amount  # long
        self.nanos = nanos  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsAmount":
        # No flags
        
        amount = Long.read(b)
        
        nanos = Int.read(b)
        
        return StarsAmount(amount=amount, nanos=nanos)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.amount))
        
        b.write(Int(self.nanos))
        
        return b.getvalue()
