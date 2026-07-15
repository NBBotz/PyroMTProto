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


class TextMentionName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``227``
        - ID: ``1A9FBFC``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["text", "user_id"]

    ID = 0x1a9fbfc
    QUALNAME = "types.TextMentionName"

    def __init__(self, *, text: "raw.base.RichText", user_id: int) -> None:
        self.text = text  # RichText
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextMentionName":
        # No flags
        
        text = TLObject.read(b)
        
        user_id = Long.read(b)
        
        return TextMentionName(text=text, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(Long(self.user_id))
        
        return b.getvalue()
