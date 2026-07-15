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


class GetAppUpdate(TLObject["raw.base.help.AppUpdate"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``522D5A7D``

    Parameters:
        source (``str``):
            N/A

    Returns:
        :obj:`help.AppUpdate <pyrogram.raw.base.help.AppUpdate>`
    """

    __slots__: list[str] = ["source"]

    ID = 0x522d5a7d
    QUALNAME = "functions.help.GetAppUpdate"

    def __init__(self, *, source: str) -> None:
        self.source = source  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAppUpdate":
        # No flags
        
        source = String.read(b)
        
        return GetAppUpdate(source=source)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.source))
        
        return b.getvalue()
