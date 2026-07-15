#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

from .message_origin import MessageOrigin

import pyrogram
from pyrogram import types, enums


class MessageOriginChannel(MessageOrigin):
    """The message was originally sent to a channel chat.

    Parameters:
        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally in Unix time

        chat (:obj:`~pyrogram.types.Chat`):
            Channel chat to which the message was originally sent
        
        message_id (``int``):
            Unique message identifier inside the chat

        author_signature (``str``, *optional*):
            Signature of the original post author

    """

    def __init__(
        self,
        *,
        date: datetime = None,
        chat: "types.Chat" = None,
        message_id: int = None,
        author_signature: str = None
    ):
        super().__init__(
            type=enums.MessageOriginType.CHANNEL,
            date=date
        )

        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature
