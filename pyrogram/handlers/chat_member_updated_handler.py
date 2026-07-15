#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Any, Callable

import pyrogram
from pyrogram.filters import Filter
from .handler import Handler

CallbackFunc: Callable = Callable[
    [
        "pyrogram.Client",
        pyrogram.types.ChatMemberUpdated
    ],
    Any
]


class ChatMemberUpdatedHandler(Handler):
    """The ChatMemberUpdated handler class. Used to handle changes in the status of a chat member.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_chat_member_updated` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new ChatMemberUpdated event arrives. It takes
            *(client, chat_member_updated)* as positional arguments (look at the section below for a detailed
            description).

        filters (:obj:`Filter`):
            Pass one or more filters to allow only a subset of updates to be passed in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the chat member updated
            handler.

        chat_member_updated (:obj:`~pyrogram.types.ChatMemberUpdated`):
            The received chat member update.

    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
