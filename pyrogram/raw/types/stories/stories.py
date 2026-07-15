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


class Stories(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.Stories`.

    Details:
        - Layer: ``227``
        - ID: ``63C3DD0A``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        stories (List of :obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        pinned_to_top (List of ``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetPinnedStories
            stories.GetStoriesArchive
            stories.GetStoriesByID
            stories.GetAlbumStories
    """

    __slots__: list[str] = ["count", "stories", "chats", "users", "pinned_to_top"]

    ID = 0x63c3dd0a
    QUALNAME = "types.stories.Stories"

    def __init__(self, *, count: int, stories: list["raw.base.StoryItem"], chats: list["raw.base.Chat"], users: list["raw.base.User"], pinned_to_top: Optional[list[int]] = None) -> None:
        self.count = count  # int
        self.stories = stories  # Vector<StoryItem>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.pinned_to_top = pinned_to_top  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Stories":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        stories = TLObject.read(b)
        
        pinned_to_top = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Stories(count=count, stories=stories, chats=chats, users=users, pinned_to_top=pinned_to_top)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned_to_top else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.stories))
        
        if self.pinned_to_top is not None:
            b.write(Vector(self.pinned_to_top, Int))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
