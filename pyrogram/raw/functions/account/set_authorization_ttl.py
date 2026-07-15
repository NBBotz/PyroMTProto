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


class SetAuthorizationTTL(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``BF899AA0``

    Parameters:
        authorization_ttl_days (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["authorization_ttl_days"]

    ID = 0xbf899aa0
    QUALNAME = "functions.account.SetAuthorizationTTL"

    def __init__(self, *, authorization_ttl_days: int) -> None:
        self.authorization_ttl_days = authorization_ttl_days  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetAuthorizationTTL":
        # No flags
        
        authorization_ttl_days = Int.read(b)
        
        return SetAuthorizationTTL(authorization_ttl_days=authorization_ttl_days)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.authorization_ttl_days))
        
        return b.getvalue()
