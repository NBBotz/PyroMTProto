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


class InlineBotWebView(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InlineBotWebView`.

    Details:
        - Layer: ``227``
        - ID: ``B57295D5``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

    """

    __slots__: list[str] = ["text", "url"]

    ID = 0xb57295d5
    QUALNAME = "types.InlineBotWebView"

    def __init__(self, *, text: str, url: str) -> None:
        self.text = text  # string
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineBotWebView":
        # No flags
        
        text = String.read(b)
        
        url = String.read(b)
        
        return InlineBotWebView(text=text, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.url))
        
        return b.getvalue()
