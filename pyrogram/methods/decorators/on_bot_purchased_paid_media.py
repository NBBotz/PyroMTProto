#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Callable

import pyrogram
from pyrogram.filters import Filter


class OnBotPurchasedPaidMedia:
    def on_bot_purchased_paid_media(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling purchased paid media updates.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.PurchasedPaidMediaHandler`.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of callback queries to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.

        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.PurchasedPaidMediaHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.PurchasedPaidMediaHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
