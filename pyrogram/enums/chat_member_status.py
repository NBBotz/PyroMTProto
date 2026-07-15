#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from enum import auto

from .auto_name import AutoName


class ChatMemberStatus(AutoName):
    """Chat member status enumeration used in :obj:`~pyrogram.types.ChatMember`."""

    OWNER = auto()  # TODO: rename to 'creator'
    "Chat owner"

    ADMINISTRATOR = auto()
    "Chat administrator"

    MEMBER = auto()
    "Chat member"

    RESTRICTED = auto()
    "Restricted chat member"

    LEFT = auto()
    "Left chat member"

    BANNED = auto()  # TODO: rename to 'kicked'
    "Banned chat member"
