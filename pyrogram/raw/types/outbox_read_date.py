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


class OutboxReadDate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.OutboxReadDate`.

    Details:
        - Layer: ``227``
        - ID: ``3BB842AC``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetOutboxReadDate
    """

    __slots__: list[str] = ["date"]

    ID = 0x3bb842ac
    QUALNAME = "types.OutboxReadDate"

    def __init__(self, *, date: int) -> None:
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "OutboxReadDate":
        # No flags
        
        date = Int.read(b)
        
        return OutboxReadDate(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        return b.getvalue()
