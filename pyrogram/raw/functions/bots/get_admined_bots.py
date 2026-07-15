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


class GetAdminedBots(TLObject["List[raw.base.User]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``B0711D83``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: list[str] = []

    ID = 0xb0711d83
    QUALNAME = "functions.bots.GetAdminedBots"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAdminedBots":
        # No flags
        
        return GetAdminedBots()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
