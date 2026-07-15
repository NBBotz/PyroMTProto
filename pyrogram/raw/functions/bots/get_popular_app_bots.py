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


class GetPopularAppBots(TLObject["raw.base.bots.PopularAppBots"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``C2510192``

    Parameters:
        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`bots.PopularAppBots <pyrogram.raw.base.bots.PopularAppBots>`
    """

    __slots__: list[str] = ["offset", "limit"]

    ID = 0xc2510192
    QUALNAME = "functions.bots.GetPopularAppBots"

    def __init__(self, *, offset: str, limit: int) -> None:
        self.offset = offset  # string
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPopularAppBots":
        # No flags
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetPopularAppBots(offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
