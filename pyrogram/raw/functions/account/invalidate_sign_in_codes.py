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


class InvalidateSignInCodes(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``CA8AE8BA``

    Parameters:
        codes (List of ``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["codes"]

    ID = 0xca8ae8ba
    QUALNAME = "functions.account.InvalidateSignInCodes"

    def __init__(self, *, codes: list[str]) -> None:
        self.codes = codes  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvalidateSignInCodes":
        # No flags
        
        codes = TLObject.read(b, String)
        
        return InvalidateSignInCodes(codes=codes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.codes, String))
        
        return b.getvalue()
