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


class VideoSizeEmojiMarkup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.VideoSize`.

    Details:
        - Layer: ``227``
        - ID: ``F85C413C``

    Parameters:
        emoji_id (``int`` ``64-bit``):
            N/A

        background_colors (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["emoji_id", "background_colors"]

    ID = 0xf85c413c
    QUALNAME = "types.VideoSizeEmojiMarkup"

    def __init__(self, *, emoji_id: int, background_colors: list[int]) -> None:
        self.emoji_id = emoji_id  # long
        self.background_colors = background_colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSizeEmojiMarkup":
        # No flags
        
        emoji_id = Long.read(b)
        
        background_colors = TLObject.read(b, Int)
        
        return VideoSizeEmojiMarkup(emoji_id=emoji_id, background_colors=background_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.emoji_id))
        
        b.write(Vector(self.background_colors, Int))
        
        return b.getvalue()
