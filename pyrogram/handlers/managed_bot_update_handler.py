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
        pyrogram.types.ManagedBotUpdated
    ],
    Any
]


class ManagedBotUpdateHandler(Handler):
    """The ManagedBotUpdate handler class.
    Used to handle new managed bot creation updates.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_managed_bot` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new ManagedBotUpdated event arrives. It takes
            *(client, managed_bot)* as positional arguments (look at the section below for a detailed
            description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of updates to be passed in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        managed_bot (:obj:`~pyrogram.types.ManagedBotUpdated`):
            A new bot was created to be managed by the bot or token of a bot was changed.

    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
