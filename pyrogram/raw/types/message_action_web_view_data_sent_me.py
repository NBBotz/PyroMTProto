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


class MessageActionWebViewDataSentMe(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``47DD8079``

    Parameters:
        text (``str``):
            N/A

        data (``str``):
            N/A

    """

    __slots__: list[str] = ["text", "data"]

    ID = 0x47dd8079
    QUALNAME = "types.MessageActionWebViewDataSentMe"

    def __init__(self, *, text: str, data: str) -> None:
        self.text = text  # string
        self.data = data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionWebViewDataSentMe":
        # No flags
        
        text = String.read(b)
        
        data = String.read(b)
        
        return MessageActionWebViewDataSentMe(text=text, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.data))
        
        return b.getvalue()
