#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

from .message_origin import MessageOrigin

import pyrogram
from pyrogram import types, enums


class MessageOriginUser(MessageOrigin):
    """The message was originally sent by a known user.

    Parameters:
        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally in Unix time

        sender_user (:obj:`~pyrogram.types.User`):
            User that sent the message originally

    """

    def __init__(
        self,
        *,
        date: datetime = None,
        sender_user: "types.User" = None
    ):
        super().__init__(
            type=enums.MessageOriginType.USER,
            date=date
        )

        self.sender_user = sender_user
