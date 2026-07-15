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


class GetPreparedInlineMessage(TLObject["raw.base.messages.PreparedInlineMessage"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``857EBDB8``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        id (``str``):
            N/A

    Returns:
        :obj:`messages.PreparedInlineMessage <pyrogram.raw.base.messages.PreparedInlineMessage>`
    """

    __slots__: list[str] = ["bot", "id"]

    ID = 0x857ebdb8
    QUALNAME = "functions.messages.GetPreparedInlineMessage"

    def __init__(self, *, bot: "raw.base.InputUser", id: str) -> None:
        self.bot = bot  # InputUser
        self.id = id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPreparedInlineMessage":
        # No flags
        
        bot = TLObject.read(b)
        
        id = String.read(b)
        
        return GetPreparedInlineMessage(bot=bot, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(String(self.id))
        
        return b.getvalue()
