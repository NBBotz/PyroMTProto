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


class GetUniqueStarGiftValueInfo(TLObject["raw.base.payments.UniqueStarGiftValueInfo"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``4365AF6B``

    Parameters:
        slug (``str``):
            N/A

    Returns:
        :obj:`payments.UniqueStarGiftValueInfo <pyrogram.raw.base.payments.UniqueStarGiftValueInfo>`
    """

    __slots__: list[str] = ["slug"]

    ID = 0x4365af6b
    QUALNAME = "functions.payments.GetUniqueStarGiftValueInfo"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUniqueStarGiftValueInfo":
        # No flags
        
        slug = String.read(b)
        
        return GetUniqueStarGiftValueInfo(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        return b.getvalue()
