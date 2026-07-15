#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

from .message_origin import MessageOrigin

import pyrogram
from pyrogram import types, enums


class MessageImportInfo(MessageOrigin):
    """Contains information about a message created with `importMessages <https://t.me/telegram/142>`_.

    Parameters:
        date (:py:obj:`~datetime.datetime`):
            Date the message was sent originally in Unix time

        sender_user_name (``str``):
            Name of the original sender

    """

    def __init__(
        self,
        *,
        date: datetime = None,
        sender_user_name: str = None
    ):
        super().__init__(
            type=enums.MessageOriginType.IMPORT_INFO,
            date=date
        )

        self.sender_user_name = sender_user_name
