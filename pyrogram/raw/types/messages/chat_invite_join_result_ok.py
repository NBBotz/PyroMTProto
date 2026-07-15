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


class ChatInviteJoinResultOk(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ChatInviteJoinResult`.

    Details:
        - Layer: ``227``
        - ID: ``445663A7``

    Parameters:
        updates (:obj:`Updates <pyrogram.raw.base.Updates>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ImportChatInvite
            channels.JoinChannel
    """

    __slots__: list[str] = ["updates"]

    ID = 0x445663a7
    QUALNAME = "types.messages.ChatInviteJoinResultOk"

    def __init__(self, *, updates: "raw.base.Updates") -> None:
        self.updates = updates  # Updates

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteJoinResultOk":
        # No flags
        
        updates = TLObject.read(b)
        
        return ChatInviteJoinResultOk(updates=updates)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.updates.write())
        
        return b.getvalue()
