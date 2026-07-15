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


class RequestPasswordRecovery(TLObject["raw.base.auth.PasswordRecovery"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``D897BC66``

    Parameters:
        No parameters required.

    Returns:
        :obj:`auth.PasswordRecovery <pyrogram.raw.base.auth.PasswordRecovery>`
    """

    __slots__: list[str] = []

    ID = 0xd897bc66
    QUALNAME = "functions.auth.RequestPasswordRecovery"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPasswordRecovery":
        # No flags
        
        return RequestPasswordRecovery()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
