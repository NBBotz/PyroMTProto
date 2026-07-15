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


class CheckQuickReplyShortcut(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``F1D0FBD3``

    Parameters:
        shortcut (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["shortcut"]

    ID = 0xf1d0fbd3
    QUALNAME = "functions.messages.CheckQuickReplyShortcut"

    def __init__(self, *, shortcut: str) -> None:
        self.shortcut = shortcut  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckQuickReplyShortcut":
        # No flags
        
        shortcut = String.read(b)
        
        return CheckQuickReplyShortcut(shortcut=shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.shortcut))
        
        return b.getvalue()
