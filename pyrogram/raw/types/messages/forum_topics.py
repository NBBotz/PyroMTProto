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


class ForumTopics(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ForumTopics`.

    Details:
        - Layer: ``227``
        - ID: ``367617D3``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        topics (List of :obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        pts (``int`` ``32-bit``):
            N/A

        order_by_create_date (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetForumTopics
            messages.GetForumTopicsByID
    """

    __slots__: list[str] = ["count", "topics", "messages", "chats", "users", "pts", "order_by_create_date"]

    ID = 0x367617d3
    QUALNAME = "types.messages.ForumTopics"

    def __init__(self, *, count: int, topics: list["raw.base.ForumTopic"], messages: list["raw.base.Message"], chats: list["raw.base.Chat"], users: list["raw.base.User"], pts: int, order_by_create_date: Optional[bool] = None) -> None:
        self.count = count  # int
        self.topics = topics  # Vector<ForumTopic>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.pts = pts  # int
        self.order_by_create_date = order_by_create_date  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopics":
        
        flags = Int.read(b)
        
        order_by_create_date = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        topics = TLObject.read(b)
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        pts = Int.read(b)
        
        return ForumTopics(count=count, topics=topics, messages=messages, chats=chats, users=users, pts=pts, order_by_create_date=order_by_create_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.order_by_create_date else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.topics))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(Int(self.pts))
        
        return b.getvalue()
