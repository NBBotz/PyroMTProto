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
        pyrogram.types.ChatJoinRequest
    ],
    Any
]


class ChatJoinRequestHandler(Handler):
    """The ChatJoinRequest handler class. Used to handle join chat requests.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_chat_join_request` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new ChatJoinRequest event arrives. It takes
            *(client, chat_join_request)* as positional arguments (look at the section below for a detailed
            description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of updates to be passed in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        chat_join_request (:obj:`~pyrogram.types.ChatJoinRequest`):
            The received chat join request.

    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
