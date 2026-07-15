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


class GetBotApp(TLObject["raw.base.messages.BotApp"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``34FDC5C3``

    Parameters:
        app (:obj:`InputBotApp <pyrogram.raw.base.InputBotApp>`):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.BotApp <pyrogram.raw.base.messages.BotApp>`
    """

    __slots__: list[str] = ["app", "hash"]

    ID = 0x34fdc5c3
    QUALNAME = "functions.messages.GetBotApp"

    def __init__(self, *, app: "raw.base.InputBotApp", hash: int) -> None:
        self.app = app  # InputBotApp
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotApp":
        # No flags
        
        app = TLObject.read(b)
        
        hash = Long.read(b)
        
        return GetBotApp(app=app, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.app.write())
        
        b.write(Long(self.hash))
        
        return b.getvalue()
