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


class GetTones(TLObject["raw.base.aicompose.Tones"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``ABD59201``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`aicompose.Tones <pyrogram.raw.base.aicompose.Tones>`
    """

    __slots__: list[str] = ["hash"]

    ID = 0xabd59201
    QUALNAME = "functions.aicompose.GetTones"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTones":
        # No flags
        
        hash = Long.read(b)
        
        return GetTones(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        return b.getvalue()
