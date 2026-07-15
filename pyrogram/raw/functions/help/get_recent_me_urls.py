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


class GetRecentMeUrls(TLObject["raw.base.help.RecentMeUrls"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``3DC0F114``

    Parameters:
        referer (``str``):
            N/A

    Returns:
        :obj:`help.RecentMeUrls <pyrogram.raw.base.help.RecentMeUrls>`
    """

    __slots__: list[str] = ["referer"]

    ID = 0x3dc0f114
    QUALNAME = "functions.help.GetRecentMeUrls"

    def __init__(self, *, referer: str) -> None:
        self.referer = referer  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentMeUrls":
        # No flags
        
        referer = String.read(b)
        
        return GetRecentMeUrls(referer=referer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.referer))
        
        return b.getvalue()
