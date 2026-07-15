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


class ChatInviteJoinResultWebView(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ChatInviteJoinResult`.

    Details:
        - Layer: ``227``
        - ID: ``2F51C337``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        webview (:obj:`WebViewResult <pyrogram.raw.base.WebViewResult>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ImportChatInvite
            channels.JoinChannel
    """

    __slots__: list[str] = ["bot_id", "webview", "users"]

    ID = 0x2f51c337
    QUALNAME = "types.messages.ChatInviteJoinResultWebView"

    def __init__(self, *, bot_id: int, webview: "raw.base.WebViewResult", users: list["raw.base.User"]) -> None:
        self.bot_id = bot_id  # long
        self.webview = webview  # WebViewResult
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteJoinResultWebView":
        # No flags
        
        bot_id = Long.read(b)
        
        webview = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatInviteJoinResultWebView(bot_id=bot_id, webview=webview, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(self.webview.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
