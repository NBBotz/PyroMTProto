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


class AdminLogResults(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.channels.AdminLogResults`.

    Details:
        - Layer: ``227``
        - ID: ``ED8AF74D``

    Parameters:
        events (List of :obj:`ChannelAdminLogEvent <pyrogram.raw.base.ChannelAdminLogEvent>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetAdminLog
    """

    __slots__: list[str] = ["events", "chats", "users"]

    ID = 0xed8af74d
    QUALNAME = "types.channels.AdminLogResults"

    def __init__(self, *, events: list["raw.base.ChannelAdminLogEvent"], chats: list["raw.base.Chat"], users: list["raw.base.User"]) -> None:
        self.events = events  # Vector<ChannelAdminLogEvent>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AdminLogResults":
        # No flags
        
        events = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return AdminLogResults(events=events, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.events))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
