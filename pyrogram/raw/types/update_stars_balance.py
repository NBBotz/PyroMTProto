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


class UpdateStarsBalance(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``4E80A379``

    Parameters:
        balance (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

    """

    __slots__: list[str] = ["balance"]

    ID = 0x4e80a379
    QUALNAME = "types.UpdateStarsBalance"

    def __init__(self, *, balance: "raw.base.StarsAmount") -> None:
        self.balance = balance  # StarsAmount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarsBalance":
        # No flags
        
        balance = TLObject.read(b)
        
        return UpdateStarsBalance(balance=balance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.balance.write())
        
        return b.getvalue()
