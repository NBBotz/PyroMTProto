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


class SendVerifyEmailCode(TLObject["raw.base.account.SentEmailCode"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``98E037BB``

    Parameters:
        purpose (:obj:`EmailVerifyPurpose <pyrogram.raw.base.EmailVerifyPurpose>`):
            N/A

        email (``str``):
            N/A

    Returns:
        :obj:`account.SentEmailCode <pyrogram.raw.base.account.SentEmailCode>`
    """

    __slots__: list[str] = ["purpose", "email"]

    ID = 0x98e037bb
    QUALNAME = "functions.account.SendVerifyEmailCode"

    def __init__(self, *, purpose: "raw.base.EmailVerifyPurpose", email: str) -> None:
        self.purpose = purpose  # EmailVerifyPurpose
        self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendVerifyEmailCode":
        # No flags
        
        purpose = TLObject.read(b)
        
        email = String.read(b)
        
        return SendVerifyEmailCode(purpose=purpose, email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        b.write(String(self.email))
        
        return b.getvalue()
