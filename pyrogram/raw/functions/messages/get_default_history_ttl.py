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


class GetDefaultHistoryTTL(TLObject["raw.base.DefaultHistoryTTL"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``658B7188``

    Parameters:
        No parameters required.

    Returns:
        :obj:`DefaultHistoryTTL <pyrogram.raw.base.DefaultHistoryTTL>`
    """

    __slots__: list[str] = []

    ID = 0x658b7188
    QUALNAME = "functions.messages.GetDefaultHistoryTTL"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDefaultHistoryTTL":
        # No flags
        
        return GetDefaultHistoryTTL()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
