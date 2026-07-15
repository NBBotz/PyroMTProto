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


class UnregisterDevice(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``6A0D3206``

    Parameters:
        token_type (``int`` ``32-bit``):
            N/A

        token (``str``):
            N/A

        other_uids (List of ``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["token_type", "token", "other_uids"]

    ID = 0x6a0d3206
    QUALNAME = "functions.account.UnregisterDevice"

    def __init__(self, *, token_type: int, token: str, other_uids: list[int]) -> None:
        self.token_type = token_type  # int
        self.token = token  # string
        self.other_uids = other_uids  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UnregisterDevice":
        # No flags
        
        token_type = Int.read(b)
        
        token = String.read(b)
        
        other_uids = TLObject.read(b, Long)
        
        return UnregisterDevice(token_type=token_type, token=token, other_uids=other_uids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.token_type))
        
        b.write(String(self.token))
        
        b.write(Vector(self.other_uids, Long))
        
        return b.getvalue()
