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


class AutoSaveSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.AutoSaveSettings`.

    Details:
        - Layer: ``227``
        - ID: ``4C3E069D``

    Parameters:
        users_settings (:obj:`AutoSaveSettings <pyrogram.raw.base.AutoSaveSettings>`):
            N/A

        chats_settings (:obj:`AutoSaveSettings <pyrogram.raw.base.AutoSaveSettings>`):
            N/A

        broadcasts_settings (:obj:`AutoSaveSettings <pyrogram.raw.base.AutoSaveSettings>`):
            N/A

        exceptions (List of :obj:`AutoSaveException <pyrogram.raw.base.AutoSaveException>`):
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

            account.GetAutoSaveSettings
    """

    __slots__: list[str] = ["users_settings", "chats_settings", "broadcasts_settings", "exceptions", "chats", "users"]

    ID = 0x4c3e069d
    QUALNAME = "types.account.AutoSaveSettings"

    def __init__(self, *, users_settings: "raw.base.AutoSaveSettings", chats_settings: "raw.base.AutoSaveSettings", broadcasts_settings: "raw.base.AutoSaveSettings", exceptions: list["raw.base.AutoSaveException"], chats: list["raw.base.Chat"], users: list["raw.base.User"]) -> None:
        self.users_settings = users_settings  # AutoSaveSettings
        self.chats_settings = chats_settings  # AutoSaveSettings
        self.broadcasts_settings = broadcasts_settings  # AutoSaveSettings
        self.exceptions = exceptions  # Vector<AutoSaveException>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoSaveSettings":
        # No flags
        
        users_settings = TLObject.read(b)
        
        chats_settings = TLObject.read(b)
        
        broadcasts_settings = TLObject.read(b)
        
        exceptions = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return AutoSaveSettings(users_settings=users_settings, chats_settings=chats_settings, broadcasts_settings=broadcasts_settings, exceptions=exceptions, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.users_settings.write())
        
        b.write(self.chats_settings.write())
        
        b.write(self.broadcasts_settings.write())
        
        b.write(Vector(self.exceptions))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
