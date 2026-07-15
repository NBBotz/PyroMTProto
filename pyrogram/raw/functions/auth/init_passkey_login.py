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


class InitPasskeyLogin(TLObject["raw.base.auth.PasskeyLoginOptions"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``518AD0B7``

    Parameters:
        api_id (``int`` ``32-bit``):
            N/A

        api_hash (``str``):
            N/A

    Returns:
        :obj:`auth.PasskeyLoginOptions <pyrogram.raw.base.auth.PasskeyLoginOptions>`
    """

    __slots__: list[str] = ["api_id", "api_hash"]

    ID = 0x518ad0b7
    QUALNAME = "functions.auth.InitPasskeyLogin"

    def __init__(self, *, api_id: int, api_hash: str) -> None:
        self.api_id = api_id  # int
        self.api_hash = api_hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitPasskeyLogin":
        # No flags
        
        api_id = Int.read(b)
        
        api_hash = String.read(b)
        
        return InitPasskeyLogin(api_id=api_id, api_hash=api_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.api_id))
        
        b.write(String(self.api_hash))
        
        return b.getvalue()
