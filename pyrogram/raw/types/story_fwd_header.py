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


class StoryFwdHeader(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryFwdHeader`.

    Details:
        - Layer: ``227``
        - ID: ``B826E150``

    Parameters:
        modified (``bool``, *optional*):
            N/A

        is_from (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        from_name (``str``, *optional*):
            N/A

        story_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["modified", "is_from", "from_name", "story_id"]

    ID = 0xb826e150
    QUALNAME = "types.StoryFwdHeader"

    def __init__(self, *, modified: Optional[bool] = None, is_from: "raw.base.Peer" = None, from_name: Optional[str] = None, story_id: Optional[int] = None) -> None:
        self.modified = modified  # flags.3?true
        self.is_from = is_from  # flags.0?Peer
        self.from_name = from_name  # flags.1?string
        self.story_id = story_id  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryFwdHeader":
        
        flags = Int.read(b)
        
        modified = True if flags & (1 << 3) else False
        is_from = TLObject.read(b) if flags & (1 << 0) else None
        
        from_name = String.read(b) if flags & (1 << 1) else None
        story_id = Int.read(b) if flags & (1 << 2) else None
        return StoryFwdHeader(modified=modified, is_from=is_from, from_name=from_name, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.modified else 0
        flags |= (1 << 0) if self.is_from is not None else 0
        flags |= (1 << 1) if self.from_name is not None else 0
        flags |= (1 << 2) if self.story_id is not None else 0
        b.write(Int(flags))
        
        if self.is_from is not None:
            b.write(self.is_from.write())
        
        if self.from_name is not None:
            b.write(String(self.from_name))
        
        if self.story_id is not None:
            b.write(Int(self.story_id))
        
        return b.getvalue()
