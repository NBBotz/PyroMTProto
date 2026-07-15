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


class BotVerification(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotVerification`.

    Details:
        - Layer: ``227``
        - ID: ``F93CD45C``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        icon (``int`` ``64-bit``):
            N/A

        description (``str``):
            N/A

    """

    __slots__: list[str] = ["bot_id", "icon", "description"]

    ID = 0xf93cd45c
    QUALNAME = "types.BotVerification"

    def __init__(self, *, bot_id: int, icon: int, description: str) -> None:
        self.bot_id = bot_id  # long
        self.icon = icon  # long
        self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotVerification":
        # No flags
        
        bot_id = Long.read(b)
        
        icon = Long.read(b)
        
        description = String.read(b)
        
        return BotVerification(bot_id=bot_id, icon=icon, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(Long(self.icon))
        
        b.write(String(self.description))
        
        return b.getvalue()
