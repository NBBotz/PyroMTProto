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


class ChatAdminsWithInvites(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ChatAdminsWithInvites`.

    Details:
        - Layer: ``227``
        - ID: ``B69B72D7``

    Parameters:
        admins (List of :obj:`ChatAdminWithInvites <pyrogram.raw.base.ChatAdminWithInvites>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAdminsWithInvites
    """

    __slots__: list[str] = ["admins", "users"]

    ID = 0xb69b72d7
    QUALNAME = "types.messages.ChatAdminsWithInvites"

    def __init__(self, *, admins: list["raw.base.ChatAdminWithInvites"], users: list["raw.base.User"]) -> None:
        self.admins = admins  # Vector<ChatAdminWithInvites>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminsWithInvites":
        # No flags
        
        admins = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatAdminsWithInvites(admins=admins, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.admins))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
