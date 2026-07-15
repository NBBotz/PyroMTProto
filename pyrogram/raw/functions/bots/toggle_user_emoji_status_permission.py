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


class ToggleUserEmojiStatusPermission(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``6DE6392``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        enabled (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["bot", "enabled"]

    ID = 0x6de6392
    QUALNAME = "functions.bots.ToggleUserEmojiStatusPermission"

    def __init__(self, *, bot: "raw.base.InputUser", enabled: bool) -> None:
        self.bot = bot  # InputUser
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUserEmojiStatusPermission":
        # No flags
        
        bot = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleUserEmojiStatusPermission(bot=bot, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
