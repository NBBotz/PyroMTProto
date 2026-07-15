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


class ChatInviteImporters(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ChatInviteImporters`.

    Details:
        - Layer: ``227``
        - ID: ``81B6B00A``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        importers (List of :obj:`ChatInviteImporter <pyrogram.raw.base.ChatInviteImporter>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetChatInviteImporters
    """

    __slots__: list[str] = ["count", "importers", "users"]

    ID = 0x81b6b00a
    QUALNAME = "types.messages.ChatInviteImporters"

    def __init__(self, *, count: int, importers: list["raw.base.ChatInviteImporter"], users: list["raw.base.User"]) -> None:
        self.count = count  # int
        self.importers = importers  # Vector<ChatInviteImporter>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteImporters":
        # No flags
        
        count = Int.read(b)
        
        importers = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatInviteImporters(count=count, importers=importers, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.importers))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
