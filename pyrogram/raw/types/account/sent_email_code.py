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


class SentEmailCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.SentEmailCode`.

    Details:
        - Layer: ``227``
        - ID: ``811F854F``

    Parameters:
        email_pattern (``str``):
            N/A

        length (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.SendVerifyEmailCode
    """

    __slots__: list[str] = ["email_pattern", "length"]

    ID = 0x811f854f
    QUALNAME = "types.account.SentEmailCode"

    def __init__(self, *, email_pattern: str, length: int) -> None:
        self.email_pattern = email_pattern  # string
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEmailCode":
        # No flags
        
        email_pattern = String.read(b)
        
        length = Int.read(b)
        
        return SentEmailCode(email_pattern=email_pattern, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email_pattern))
        
        b.write(Int(self.length))
        
        return b.getvalue()
