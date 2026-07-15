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


class BusinessAwayMessageScheduleCustom(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BusinessAwayMessageSchedule`.

    Details:
        - Layer: ``227``
        - ID: ``CC4D9ECC``

    Parameters:
        start_date (``int`` ``32-bit``):
            N/A

        end_date (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["start_date", "end_date"]

    ID = 0xcc4d9ecc
    QUALNAME = "types.BusinessAwayMessageScheduleCustom"

    def __init__(self, *, start_date: int, end_date: int) -> None:
        self.start_date = start_date  # int
        self.end_date = end_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessAwayMessageScheduleCustom":
        # No flags
        
        start_date = Int.read(b)
        
        end_date = Int.read(b)
        
        return BusinessAwayMessageScheduleCustom(start_date=start_date, end_date=end_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.start_date))
        
        b.write(Int(self.end_date))
        
        return b.getvalue()
