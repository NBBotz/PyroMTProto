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


class UpdateTone(TLObject["raw.base.AiComposeTone"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``903BCF59``

    Parameters:
        tone (:obj:`InputAiComposeTone <pyrogram.raw.base.InputAiComposeTone>`):
            N/A

        display_author (``bool``, *optional*):
            N/A

        emoji_id (``int`` ``64-bit``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        prompt (``str``, *optional*):
            N/A

    Returns:
        :obj:`AiComposeTone <pyrogram.raw.base.AiComposeTone>`
    """

    __slots__: list[str] = ["tone", "display_author", "emoji_id", "title", "prompt"]

    ID = 0x903bcf59
    QUALNAME = "functions.aicompose.UpdateTone"

    def __init__(self, *, tone: "raw.base.InputAiComposeTone", display_author: Optional[bool] = None, emoji_id: Optional[int] = None, title: Optional[str] = None, prompt: Optional[str] = None) -> None:
        self.tone = tone  # InputAiComposeTone
        self.display_author = display_author  # flags.0?Bool
        self.emoji_id = emoji_id  # flags.1?long
        self.title = title  # flags.2?string
        self.prompt = prompt  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTone":
        
        flags = Int.read(b)
        
        tone = TLObject.read(b)
        
        display_author = Bool.read(b) if flags & (1 << 0) else None
        emoji_id = Long.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 2) else None
        prompt = String.read(b) if flags & (1 << 3) else None
        return UpdateTone(tone=tone, display_author=display_author, emoji_id=emoji_id, title=title, prompt=prompt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.display_author is not None else 0
        flags |= (1 << 1) if self.emoji_id is not None else 0
        flags |= (1 << 2) if self.title is not None else 0
        flags |= (1 << 3) if self.prompt is not None else 0
        b.write(Int(flags))
        
        b.write(self.tone.write())
        
        if self.display_author is not None:
            b.write(Bool(self.display_author))
        
        if self.emoji_id is not None:
            b.write(Long(self.emoji_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.prompt is not None:
            b.write(String(self.prompt))
        
        return b.getvalue()
