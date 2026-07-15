#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import inspect
from typing import Any, Callable

import pyrogram
from pyrogram.filters import Filter
from pyrogram.types import Update

CallbackFunc: Callable = Callable[..., Any]


class Handler:
    def __init__(self, callback: CallbackFunc, filters: Filter = None):
        self.callback = callback
        self.filters = filters

    async def check(self, client: "pyrogram.Client", update: Update):
        if callable(self.filters):
            if inspect.iscoroutinefunction(self.filters.__call__):
                return await self.filters(client, update)
            else:
                return await client.loop.run_in_executor(
                    client.executor,
                    self.filters,
                    client, update
                )

        return True
