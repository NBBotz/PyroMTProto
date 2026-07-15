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


class ResetPasswordRequestedWait(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.ResetPasswordResult`.

    Details:
        - Layer: ``227``
        - ID: ``E9EFFC7D``

    Parameters:
        until_date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    __slots__: list[str] = ["until_date"]

    ID = 0xe9effc7d
    QUALNAME = "types.account.ResetPasswordRequestedWait"

    def __init__(self, *, until_date: int) -> None:
        self.until_date = until_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPasswordRequestedWait":
        # No flags
        
        until_date = Int.read(b)
        
        return ResetPasswordRequestedWait(until_date=until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.until_date))
        
        return b.getvalue()
