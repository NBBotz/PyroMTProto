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


class GetBotInfo(TLObject["raw.base.bots.BotInfo"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``DCD914FD``

    Parameters:
        lang_code (``str``):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        :obj:`bots.BotInfo <pyrogram.raw.base.bots.BotInfo>`
    """

    __slots__: list[str] = ["lang_code", "bot"]

    ID = 0xdcd914fd
    QUALNAME = "functions.bots.GetBotInfo"

    def __init__(self, *, lang_code: str, bot: "raw.base.InputUser" = None) -> None:
        self.lang_code = lang_code  # string
        self.bot = bot  # flags.0?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotInfo":
        
        flags = Int.read(b)
        
        bot = TLObject.read(b) if flags & (1 << 0) else None
        
        lang_code = String.read(b)
        
        return GetBotInfo(lang_code=lang_code, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.bot is not None else 0
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(String(self.lang_code))
        
        return b.getvalue()
