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
        pyrogram.types.PreCheckoutQuery
    ],
    Any
]


class PreCheckoutQueryHandler(Handler):
    """The PreCheckoutQueryHandler handler class. Used to handle pre-checkout queries coming from invoice buttons.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_pre_checkout_query` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new PreCheckoutQuery arrives. It takes *(client, pre_checkout_query)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of callback queries to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        pre_checkout_query (:obj:`~pyrogram.types.PreCheckoutQuery`):
            New incoming pre-checkout query. Contains full information about checkout.

    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
