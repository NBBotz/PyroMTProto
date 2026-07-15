#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

from .message_origin import MessageOrigin

import pyrogram
from pyrogram import types, enums


class MessageOriginChat(MessageOrigin):
    """The message was originally sent on behalf of a chat to a group chat.

    Parameters:
        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally in Unix time

        sender_chat (:obj:`~pyrogram.types.Chat`):
            Chat that sent the message originally
        
        author_signature (``str``, *optional*):
            For messages originally sent by an anonymous chat administrator, original message author signature

    """

    def __init__(
        self,
        *,
        date: datetime = None,
        sender_chat: "types.Chat" = None,
        author_signature: str = None
    ):
        super().__init__(
            type=enums.MessageOriginType.CHAT,
            date=date
        )

        self.sender_chat = sender_chat
        self.author_signature = author_signature
