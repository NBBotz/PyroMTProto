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


class SearchEmojiStickerSets(TLObject["raw.base.messages.FoundStickerSets"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``92B4494C``

    Parameters:
        q (``str``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        exclude_featured (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.FoundStickerSets <pyrogram.raw.base.messages.FoundStickerSets>`
    """

    __slots__: list[str] = ["q", "hash", "exclude_featured"]

    ID = 0x92b4494c
    QUALNAME = "functions.messages.SearchEmojiStickerSets"

    def __init__(self, *, q: str, hash: int, exclude_featured: Optional[bool] = None) -> None:
        self.q = q  # string
        self.hash = hash  # long
        self.exclude_featured = exclude_featured  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchEmojiStickerSets":
        
        flags = Int.read(b)
        
        exclude_featured = True if flags & (1 << 0) else False
        q = String.read(b)
        
        hash = Long.read(b)
        
        return SearchEmojiStickerSets(q=q, hash=hash, exclude_featured=exclude_featured)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_featured else 0
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
