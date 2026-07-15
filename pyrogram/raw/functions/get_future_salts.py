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


class GetFutureSalts(TLObject["raw.base.FutureSalts"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``B921BD04``

    Parameters:
        num (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`FutureSalts <pyrogram.raw.base.FutureSalts>`
    """

    __slots__: list[str] = ["num"]

    ID = 0xb921bd04
    QUALNAME = "functions.GetFutureSalts"

    def __init__(self, *, num: int) -> None:
        self.num = num  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFutureSalts":
        # No flags
        
        num = Int.read(b)
        
        return GetFutureSalts(num=num)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.num))
        
        return b.getvalue()
