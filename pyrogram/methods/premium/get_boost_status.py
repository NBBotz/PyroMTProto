#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class GetBoostStatus:
    async def get_boost_status(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ):
        """Get the current boost status of a channel or supergroup.

        Returns information about the channel's boost level, number of
        boosts, next level requirements, and active giveaways.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier or username of the target channel/group.

        Returns:
            :obj:`~pyrogram.raw.types.premium.BoostsStatus` with fields:
            ``level``, ``boosts``, ``current_level_boosts``,
            ``next_level_boosts``, ``boost_url``, ``prepaid_giveaways``.

        Example:
            .. code-block:: python

                status = await app.get_boost_status("@mychannel")
                print(f"Level: {status.level}, Boosts: {status.boosts}")
        """
        peer = await self.resolve_peer(chat_id)
        return await self.invoke(
            raw.functions.premium.GetBoostsStatus(peer=peer)
        )
