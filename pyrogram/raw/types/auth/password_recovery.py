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


class PasswordRecovery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.PasswordRecovery`.

    Details:
        - Layer: ``227``
        - ID: ``137948A5``

    Parameters:
        email_pattern (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.RequestPasswordRecovery
    """

    __slots__: list[str] = ["email_pattern"]

    ID = 0x137948a5
    QUALNAME = "types.auth.PasswordRecovery"

    def __init__(self, *, email_pattern: str) -> None:
        self.email_pattern = email_pattern  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordRecovery":
        # No flags
        
        email_pattern = String.read(b)
        
        return PasswordRecovery(email_pattern=email_pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email_pattern))
        
        return b.getvalue()
