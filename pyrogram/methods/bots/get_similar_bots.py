#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw, types


class GetSimilarBots:
    async def get_similar_bots(
        self: "pyrogram.Client",
        user_id: Union[int, str]
    ) -> list["types.User"]:
        """Returns a list of bots similar to the given bot.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target bot.

        Returns:
            List of :obj:`~pyrogram.types.User`: On success.

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        Example:
            .. code-block:: python

                bots = await app.get_similar_bots()
        """

        botss = await self.invoke(raw.functions.bots.GetBotRecommendations(
            bot=await self.resolve_peer(user_id)
        ))
        return types.List([
            types.User._parse(self, b)
            for b in botss.users
        ])
