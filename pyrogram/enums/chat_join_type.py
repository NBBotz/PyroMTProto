#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from enum import auto

from .auto_name import AutoName


class ChatJoinType(AutoName):
    """How the service message :obj:`~pyrogram.enums.MessageServiceType.NEW_CHAT_MEMBERS` was used for the member to join the chat."""

    BY_ADD = auto()
    "New chat members were added. ``from_user`` will contain the actor. ``new_chat_members`` will contain the user identifiers of the new members."

    BY_LINK = auto()
    "A new member joined the chat via an invite link"

    BY_REQUEST = auto()
    "A new member was accepted to the chat by an administrator"
