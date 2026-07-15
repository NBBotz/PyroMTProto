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
        pyrogram.types.User
    ],
    Any
]


class UserStatusHandler(Handler):
    """The UserStatus handler class. Used to handle user status updates (user going online or offline).
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the :meth:`~pyrogram.Client.on_user_status` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new user status update arrives. It takes *(client, user)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filter`):
            Pass one or more filters to allow only a subset of users to be passed in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the user status handler.

        user (:obj:`~pyrogram.types.User`):
            The user containing the updated status.
    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
