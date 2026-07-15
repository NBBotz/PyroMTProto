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
        pyrogram.types.ChosenInlineResult
    ],
    Any
]


class ChosenInlineResultHandler(Handler):
    """The ChosenInlineResultHandler handler class. Used to handle chosen inline results coming from inline queries.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    Please see the official documentation on the `feedback collecting <https://core.telegram.org/bots/inline#collecting-feedback>`_ for details on how to enable these updates for your bot.

    `This should only be used for statistical purposes, rather than functional <https://core.telegram.org/api/bots/inline#inline-feedback>`_.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_chosen_inline_result` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new chosen inline result arrives.
            It takes *(client, chosen_inline_result)* as positional arguments (look at the section below for a
            detailed description).

        filters (:obj:`Filter`):
            Pass one or more filters to allow only a subset of chosen inline results to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the choose inline result
            handler.

        chosen_inline_result (:obj:`~pyrogram.types.ChosenInlineResult`):
            The received chosen inline result.

    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
