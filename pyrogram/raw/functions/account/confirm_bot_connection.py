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


class ConfirmBotConnection(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``67ED1F68``

    Parameters:
        bot_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["bot_id"]

    ID = 0x67ed1f68
    QUALNAME = "functions.account.ConfirmBotConnection"

    def __init__(self, *, bot_id: "raw.base.InputUser") -> None:
        self.bot_id = bot_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmBotConnection":
        # No flags
        
        bot_id = TLObject.read(b)
        
        return ConfirmBotConnection(bot_id=bot_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot_id.write())
        
        return b.getvalue()
