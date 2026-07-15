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


class ExportedInvites(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.chatlists.ExportedInvites`.

    Details:
        - Layer: ``227``
        - ID: ``10AB6DC7``

    Parameters:
        invites (List of :obj:`ExportedChatlistInvite <pyrogram.raw.base.ExportedChatlistInvite>`):
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

            chatlists.GetExportedInvites
    """

    __slots__: list[str] = ["invites", "chats", "users"]

    ID = 0x10ab6dc7
    QUALNAME = "types.chatlists.ExportedInvites"

    def __init__(self, *, invites: list["raw.base.ExportedChatlistInvite"], chats: list["raw.base.Chat"], users: list["raw.base.User"]) -> None:
        self.invites = invites  # Vector<ExportedChatlistInvite>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedInvites":
        # No flags
        
        invites = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ExportedInvites(invites=invites, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.invites))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
