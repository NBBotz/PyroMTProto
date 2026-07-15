#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional, AsyncGenerator
import pyrogram
from pyrogram import raw


class GetBoostsList:
    async def get_boosts_list(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        gifts: bool = False,
        offset: str = "",
        limit: int = 100,
    ) -> AsyncGenerator:
        """Get the list of users who boosted a channel/group.

        Parameters:
            chat_id (``int`` | ``str``):
                The channel or group to get boosters for.

            gifts (``bool``, *optional*):
                If True, return only boosts from giveaway gifts.
                Defaults to False (all boosts).

            offset (``str``, *optional*):
                Pagination offset from previous call.

            limit (``int``, *optional*):
                Maximum number of boosts to return. Defaults to 100.

        Yields:
            :obj:`~pyrogram.raw.types.Boost` for each booster.

        Example:
            .. code-block:: python

                async for boost in app.get_boosts_list("@channel"):
                    print(boost.user_id, boost.expires)
        """
        peer = await self.resolve_peer(chat_id)

        while True:
            r = await self.invoke(
                raw.functions.premium.GetBoostsList(
                    peer=peer,
                    gifts=gifts,
                    offset=offset,
                    limit=min(limit, 100),
                )
            )

            for boost in r.boosts:
                yield boost
                limit -= 1
                if limit == 0:
                    return

            if not r.next_offset:
                break
            offset = r.next_offset
