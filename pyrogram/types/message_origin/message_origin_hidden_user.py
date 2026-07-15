#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

from .message_origin import MessageOrigin

import pyrogram
from pyrogram import types, enums


class MessageOriginHiddenUser(MessageOrigin):
    """The message was originally sent by an unknown user.

    Parameters:
        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally in Unix time

        sender_user_name (``str``):
            Name of the user that sent the message originally

    """

    def __init__(
        self,
        *,
        date: datetime = None,
        sender_user_name: str = None
    ):
        super().__init__(
            type=enums.MessageOriginType.HIDDEN_USER,
            date=date
        )

        self.sender_user_name = sender_user_name
