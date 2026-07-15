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


class DiscussionMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.DiscussionMessage`.

    Details:
        - Layer: ``227``
        - ID: ``A6341782``

    Parameters:
        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        unread_count (``int`` ``32-bit``):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        max_id (``int`` ``32-bit``, *optional*):
            N/A

        read_inbox_max_id (``int`` ``32-bit``, *optional*):
            N/A

        read_outbox_max_id (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDiscussionMessage
    """

    __slots__: list[str] = ["messages", "unread_count", "chats", "users", "max_id", "read_inbox_max_id", "read_outbox_max_id"]

    ID = 0xa6341782
    QUALNAME = "types.messages.DiscussionMessage"

    def __init__(self, *, messages: list["raw.base.Message"], unread_count: int, chats: list["raw.base.Chat"], users: list["raw.base.User"], max_id: Optional[int] = None, read_inbox_max_id: Optional[int] = None, read_outbox_max_id: Optional[int] = None) -> None:
        self.messages = messages  # Vector<Message>
        self.unread_count = unread_count  # int
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.max_id = max_id  # flags.0?int
        self.read_inbox_max_id = read_inbox_max_id  # flags.1?int
        self.read_outbox_max_id = read_outbox_max_id  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DiscussionMessage":
        
        flags = Int.read(b)
        
        messages = TLObject.read(b)
        
        max_id = Int.read(b) if flags & (1 << 0) else None
        read_inbox_max_id = Int.read(b) if flags & (1 << 1) else None
        read_outbox_max_id = Int.read(b) if flags & (1 << 2) else None
        unread_count = Int.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return DiscussionMessage(messages=messages, unread_count=unread_count, chats=chats, users=users, max_id=max_id, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.max_id is not None else 0
        flags |= (1 << 1) if self.read_inbox_max_id is not None else 0
        flags |= (1 << 2) if self.read_outbox_max_id is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.messages))
        
        if self.max_id is not None:
            b.write(Int(self.max_id))
        
        if self.read_inbox_max_id is not None:
            b.write(Int(self.read_inbox_max_id))
        
        if self.read_outbox_max_id is not None:
            b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
