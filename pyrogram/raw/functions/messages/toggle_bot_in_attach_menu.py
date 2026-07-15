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


class ToggleBotInAttachMenu(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``69F59D69``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        enabled (``bool``):
            N/A

        write_allowed (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["bot", "enabled", "write_allowed"]

    ID = 0x69f59d69
    QUALNAME = "functions.messages.ToggleBotInAttachMenu"

    def __init__(self, *, bot: "raw.base.InputUser", enabled: bool, write_allowed: Optional[bool] = None) -> None:
        self.bot = bot  # InputUser
        self.enabled = enabled  # Bool
        self.write_allowed = write_allowed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleBotInAttachMenu":
        
        flags = Int.read(b)
        
        write_allowed = True if flags & (1 << 0) else False
        bot = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleBotInAttachMenu(bot=bot, enabled=enabled, write_allowed=write_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.write_allowed else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
