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


class SetAccountTTL(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``2442485E``

    Parameters:
        ttl (:obj:`AccountDaysTTL <pyrogram.raw.base.AccountDaysTTL>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["ttl"]

    ID = 0x2442485e
    QUALNAME = "functions.account.SetAccountTTL"

    def __init__(self, *, ttl: "raw.base.AccountDaysTTL") -> None:
        self.ttl = ttl  # AccountDaysTTL

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetAccountTTL":
        # No flags
        
        ttl = TLObject.read(b)
        
        return SetAccountTTL(ttl=ttl)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.ttl.write())
        
        return b.getvalue()
