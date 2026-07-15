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


class SetMainProfileTab(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``5DEE78B0``

    Parameters:
        tab (:obj:`ProfileTab <pyrogram.raw.base.ProfileTab>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["tab"]

    ID = 0x5dee78b0
    QUALNAME = "functions.account.SetMainProfileTab"

    def __init__(self, *, tab: "raw.base.ProfileTab") -> None:
        self.tab = tab  # ProfileTab

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetMainProfileTab":
        # No flags
        
        tab = TLObject.read(b)
        
        return SetMainProfileTab(tab=tab)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.tab.write())
        
        return b.getvalue()
