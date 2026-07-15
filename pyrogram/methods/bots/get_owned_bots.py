#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types


class GetOwnedBots:
    async def get_owned_bots(
        self: "pyrogram.Client",
    ) -> list["types.User"]:
        """Returns the list of bots owned by the current user.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.User`: On success.

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        Example:
            .. code-block:: python

                bots = await app.get_owned_bots()
        """

        bots = await self.invoke(raw.functions.bots.GetAdminedBots())
        return types.List([
            types.User._parse(self, b)
            for b in bots
        ])
