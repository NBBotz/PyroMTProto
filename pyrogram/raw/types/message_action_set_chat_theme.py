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


class MessageActionSetChatTheme(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``B91BBD3A``

    Parameters:
        theme (:obj:`ChatTheme <pyrogram.raw.base.ChatTheme>`):
            N/A

    """

    __slots__: list[str] = ["theme"]

    ID = 0xb91bbd3a
    QUALNAME = "types.MessageActionSetChatTheme"

    def __init__(self, *, theme: "raw.base.ChatTheme") -> None:
        self.theme = theme  # ChatTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetChatTheme":
        # No flags
        
        theme = TLObject.read(b)
        
        return MessageActionSetChatTheme(theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.theme.write())
        
        return b.getvalue()
