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


class AttachMenuBotsBot(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBotsBot`.

    Details:
        - Layer: ``227``
        - ID: ``93BF667F``

    Parameters:
        bot (:obj:`AttachMenuBot <pyrogram.raw.base.AttachMenuBot>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBot
    """

    __slots__: list[str] = ["bot", "users"]

    ID = 0x93bf667f
    QUALNAME = "types.AttachMenuBotsBot"

    def __init__(self, *, bot: "raw.base.AttachMenuBot", users: list["raw.base.User"]) -> None:
        self.bot = bot  # AttachMenuBot
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotsBot":
        # No flags
        
        bot = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return AttachMenuBotsBot(bot=bot, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
