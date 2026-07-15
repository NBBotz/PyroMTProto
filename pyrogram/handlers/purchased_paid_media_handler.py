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
        pyrogram.types.PaidMediaPurchased
    ],
    Any
]


class PurchasedPaidMediaHandler(Handler):
    """The Bot Business Connection handler class. Used to handle new bot business connection.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_bot_purchased_paid_media` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new PaidMediaPurchased arrives. It takes *(client, purchased_paid_media)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of callback queries to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        purchased_paid_media (:obj:`~pyrogram.types.PaidMediaPurchased`):
            A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat.

    """

    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        super().__init__(callback, filters)
