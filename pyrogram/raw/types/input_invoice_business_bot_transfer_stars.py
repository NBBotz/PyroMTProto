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


class InputInvoiceBusinessBotTransferStars(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``227``
        - ID: ``F4997E42``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        stars (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["bot", "stars"]

    ID = 0xf4997e42
    QUALNAME = "types.InputInvoiceBusinessBotTransferStars"

    def __init__(self, *, bot: "raw.base.InputUser", stars: int) -> None:
        self.bot = bot  # InputUser
        self.stars = stars  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceBusinessBotTransferStars":
        # No flags
        
        bot = TLObject.read(b)
        
        stars = Long.read(b)
        
        return InputInvoiceBusinessBotTransferStars(bot=bot, stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Long(self.stars))
        
        return b.getvalue()
