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


class AiComposeToneDefault(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AiComposeTone`.

    Details:
        - Layer: ``227``
        - ID: ``9BAD6414``

    Parameters:
        tone (``str``):
            N/A

        emoji_id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            aicompose.CreateTone
            aicompose.UpdateTone
    """

    __slots__: list[str] = ["tone", "emoji_id", "title"]

    ID = 0x9bad6414
    QUALNAME = "types.AiComposeToneDefault"

    def __init__(self, *, tone: str, emoji_id: int, title: str) -> None:
        self.tone = tone  # string
        self.emoji_id = emoji_id  # long
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AiComposeToneDefault":
        # No flags
        
        tone = String.read(b)
        
        emoji_id = Long.read(b)
        
        title = String.read(b)
        
        return AiComposeToneDefault(tone=tone, emoji_id=emoji_id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.tone))
        
        b.write(Long(self.emoji_id))
        
        b.write(String(self.title))
        
        return b.getvalue()
