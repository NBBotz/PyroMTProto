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


class ExportBotToken(TLObject["raw.base.bots.ExportedBotToken"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``BD0D99EB``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        revoke (``bool``):
            N/A

    Returns:
        :obj:`bots.ExportedBotToken <pyrogram.raw.base.bots.ExportedBotToken>`
    """

    __slots__: list[str] = ["bot", "revoke"]

    ID = 0xbd0d99eb
    QUALNAME = "functions.bots.ExportBotToken"

    def __init__(self, *, bot: "raw.base.InputUser", revoke: bool) -> None:
        self.bot = bot  # InputUser
        self.revoke = revoke  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportBotToken":
        # No flags
        
        bot = TLObject.read(b)
        
        revoke = Bool.read(b)
        
        return ExportBotToken(bot=bot, revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Bool(self.revoke))
        
        return b.getvalue()
