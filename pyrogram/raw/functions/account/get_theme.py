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


class GetTheme(TLObject["raw.base.Theme"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``3A5869EC``

    Parameters:
        format (``str``):
            N/A

        theme (:obj:`InputTheme <pyrogram.raw.base.InputTheme>`):
            N/A

    Returns:
        :obj:`Theme <pyrogram.raw.base.Theme>`
    """

    __slots__: list[str] = ["format", "theme"]

    ID = 0x3a5869ec
    QUALNAME = "functions.account.GetTheme"

    def __init__(self, *, format: str, theme: "raw.base.InputTheme") -> None:
        self.format = format  # string
        self.theme = theme  # InputTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTheme":
        # No flags
        
        format = String.read(b)
        
        theme = TLObject.read(b)
        
        return GetTheme(format=format, theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        return b.getvalue()
