#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class GetMyBoosts:
    async def get_my_boosts(self: "pyrogram.Client"):
        """Get all channels/groups you are currently boosting.

        Returns information about your active boost slots,
        including which chats each slot is applied to and
        when each boost expires.

        Returns:
            :obj:`~pyrogram.raw.types.premium.MyBoosts` with
            ``my_boosts`` (list of :obj:`~pyrogram.raw.types.MyBoost`),
            ``users``, and ``chats``.

        Example:
            .. code-block:: python

                boosts = await app.get_my_boosts()
                for b in boosts.my_boosts:
                    print(f"Slot {b.slot}: expires {b.expires}")
        """
        return await self.invoke(
            raw.functions.premium.GetMyBoosts()
        )
