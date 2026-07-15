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


class ReorderPreviewMedias(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``B627F3AA``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        lang_code (``str``):
            N/A

        order (List of :obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["bot", "lang_code", "order"]

    ID = 0xb627f3aa
    QUALNAME = "functions.bots.ReorderPreviewMedias"

    def __init__(self, *, bot: "raw.base.InputUser", lang_code: str, order: list["raw.base.InputMedia"]) -> None:
        self.bot = bot  # InputUser
        self.lang_code = lang_code  # string
        self.order = order  # Vector<InputMedia>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPreviewMedias":
        # No flags
        
        bot = TLObject.read(b)
        
        lang_code = String.read(b)
        
        order = TLObject.read(b)
        
        return ReorderPreviewMedias(bot=bot, lang_code=lang_code, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(String(self.lang_code))
        
        b.write(Vector(self.order))
        
        return b.getvalue()
