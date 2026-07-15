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


class SavedReactionTag(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SavedReactionTag`.

    Details:
        - Layer: ``227``
        - ID: ``CB6FF828``

    Parameters:
        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

        count (``int`` ``32-bit``):
            N/A

        title (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["reaction", "count", "title"]

    ID = 0xcb6ff828
    QUALNAME = "types.SavedReactionTag"

    def __init__(self, *, reaction: "raw.base.Reaction", count: int, title: Optional[str] = None) -> None:
        self.reaction = reaction  # Reaction
        self.count = count  # int
        self.title = title  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedReactionTag":
        
        flags = Int.read(b)
        
        reaction = TLObject.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        count = Int.read(b)
        
        return SavedReactionTag(reaction=reaction, count=count, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        b.write(Int(flags))
        
        b.write(self.reaction.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        b.write(Int(self.count))
        
        return b.getvalue()
