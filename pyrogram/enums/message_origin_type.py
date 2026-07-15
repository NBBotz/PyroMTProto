#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from enum import auto

from .auto_name import AutoName


class MessageOriginType(AutoName):
    """Message origin type enumeration used in :obj:`~pyrogram.types.MessageOrigin`."""

    CHANNEL = auto()
    "The message was originally a post in a channel"

    CHAT = auto()
    "The message was originally sent on behalf of a chat"

    HIDDEN_USER = auto()
    "The message was originally sent by a user, which is hidden by their privacy settings"

    IMPORT_INFO = auto()
    "The message was imported with `importMessages <https://t.me/telegram/142>`_"

    USER = auto()
    "The message was originally sent by a known user"
