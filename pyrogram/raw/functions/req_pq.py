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


class ReqPq(TLObject["raw.base.ResPQ"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``60469778``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

    Returns:
        :obj:`ResPQ <pyrogram.raw.base.ResPQ>`
    """

    __slots__: list[str] = ["nonce"]

    ID = 0x60469778
    QUALNAME = "functions.ReqPq"

    def __init__(self, *, nonce: int) -> None:
        self.nonce = nonce  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReqPq":
        # No flags
        
        nonce = Int128.read(b)
        
        return ReqPq(nonce=nonce)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        return b.getvalue()
