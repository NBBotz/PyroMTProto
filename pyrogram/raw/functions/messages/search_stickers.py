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


class SearchStickers(TLObject["raw.base.messages.FoundStickers"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``29B1C66A``

    Parameters:
        q (``str``):
            N/A

        emoticon (``str``):
            N/A

        lang_code (List of ``str``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        emojis (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.FoundStickers <pyrogram.raw.base.messages.FoundStickers>`
    """

    __slots__: list[str] = ["q", "emoticon", "lang_code", "offset", "limit", "hash", "emojis"]

    ID = 0x29b1c66a
    QUALNAME = "functions.messages.SearchStickers"

    def __init__(self, *, q: str, emoticon: str, lang_code: list[str], offset: int, limit: int, hash: int, emojis: Optional[bool] = None) -> None:
        self.q = q  # string
        self.emoticon = emoticon  # string
        self.lang_code = lang_code  # Vector<string>
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # long
        self.emojis = emojis  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchStickers":
        
        flags = Int.read(b)
        
        emojis = True if flags & (1 << 0) else False
        q = String.read(b)
        
        emoticon = String.read(b)
        
        lang_code = TLObject.read(b, String)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return SearchStickers(q=q, emoticon=emoticon, lang_code=lang_code, offset=offset, limit=limit, hash=hash, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.emojis else 0
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(String(self.emoticon))
        
        b.write(Vector(self.lang_code, String))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
