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


class JoinChatBotResultWebView(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JoinChatBotResult`.

    Details:
        - Layer: ``227``
        - ID: ``D6E3B813``

    Parameters:
        url (``str``):
            N/A

    """

    __slots__: list[str] = ["url"]

    ID = 0xd6e3b813
    QUALNAME = "types.JoinChatBotResultWebView"

    def __init__(self, *, url: str) -> None:
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinChatBotResultWebView":
        # No flags
        
        url = String.read(b)
        
        return JoinChatBotResultWebView(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        return b.getvalue()
