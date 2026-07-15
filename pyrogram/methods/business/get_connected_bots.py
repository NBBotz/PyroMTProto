#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetConnectedBots:
    async def get_connected_bots(
        self: "pyrogram.Client",
    ) -> "types.ConnectedBots":
        """Get bots connected to your business account.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.types.ConnectedBots`

        Example:
            .. code-block:: python

                await app.get_connected_bots(...)
        """

        r = await self.invoke(
            raw.functions.account.getConnectedBots(

            )
        )

        return types.ConnectedBots._parse(self, r)
