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


class CheckUrlAuthMatchCode(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``C9A47B0B``

    Parameters:
        url (``str``):
            N/A

        match_code (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["url", "match_code"]

    ID = 0xc9a47b0b
    QUALNAME = "functions.messages.CheckUrlAuthMatchCode"

    def __init__(self, *, url: str, match_code: str) -> None:
        self.url = url  # string
        self.match_code = match_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckUrlAuthMatchCode":
        # No flags
        
        url = String.read(b)
        
        match_code = String.read(b)
        
        return CheckUrlAuthMatchCode(url=url, match_code=match_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(String(self.match_code))
        
        return b.getvalue()
