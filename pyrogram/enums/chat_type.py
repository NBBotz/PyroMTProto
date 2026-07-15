#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from enum import auto

from .auto_name import AutoName


class ChatType(AutoName):
    """Chat type enumeration used in :obj:`~pyrogram.types.Chat`."""

    PRIVATE = auto()
    "Chat is a private chat with a user"

    BOT = auto()
    "Chat is a private chat with a bot"

    GROUP = auto()
    "Chat is a group"

    SUPERGROUP = auto()
    "Chat is a supergroup"

    CHANNEL = auto()
    "Chat is a channel"
