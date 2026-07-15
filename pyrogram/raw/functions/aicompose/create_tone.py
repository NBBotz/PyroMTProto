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


class CreateTone(TLObject["raw.base.AiComposeTone"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``4AA83913``

    Parameters:
        emoji_id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

        prompt (``str``):
            N/A

        display_author (``bool``, *optional*):
            N/A

    Returns:
        :obj:`AiComposeTone <pyrogram.raw.base.AiComposeTone>`
    """

    __slots__: list[str] = ["emoji_id", "title", "prompt", "display_author"]

    ID = 0x4aa83913
    QUALNAME = "functions.aicompose.CreateTone"

    def __init__(self, *, emoji_id: int, title: str, prompt: str, display_author: Optional[bool] = None) -> None:
        self.emoji_id = emoji_id  # long
        self.title = title  # string
        self.prompt = prompt  # string
        self.display_author = display_author  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateTone":
        
        flags = Int.read(b)
        
        display_author = True if flags & (1 << 0) else False
        emoji_id = Long.read(b)
        
        title = String.read(b)
        
        prompt = String.read(b)
        
        return CreateTone(emoji_id=emoji_id, title=title, prompt=prompt, display_author=display_author)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.display_author else 0
        b.write(Int(flags))
        
        b.write(Long(self.emoji_id))
        
        b.write(String(self.title))
        
        b.write(String(self.prompt))
        
        return b.getvalue()
