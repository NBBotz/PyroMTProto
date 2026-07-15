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


class EditAccessSettings(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``31813CD8``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        restricted (``bool``, *optional*):
            N/A

        add_users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["bot", "restricted", "add_users"]

    ID = 0x31813cd8
    QUALNAME = "functions.bots.EditAccessSettings"

    def __init__(self, *, bot: "raw.base.InputUser", restricted: Optional[bool] = None, add_users: Optional[list["raw.base.InputUser"]] = None) -> None:
        self.bot = bot  # InputUser
        self.restricted = restricted  # flags.0?true
        self.add_users = add_users  # flags.1?Vector<InputUser>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditAccessSettings":
        
        flags = Int.read(b)
        
        restricted = True if flags & (1 << 0) else False
        bot = TLObject.read(b)
        
        add_users = TLObject.read(b) if flags & (1 << 1) else []
        
        return EditAccessSettings(bot=bot, restricted=restricted, add_users=add_users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.restricted else 0
        flags |= (1 << 1) if self.add_users else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        if self.add_users is not None:
            b.write(Vector(self.add_users))
        
        return b.getvalue()
