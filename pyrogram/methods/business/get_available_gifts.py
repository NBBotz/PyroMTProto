#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw, types


class GetAvailableGifts:
    async def get_available_gifts(
        self: "pyrogram.Client",
    ) -> list[Union["types.Gift", "types.UpgradedGift"]]:
        """Get all gifts that can be sent to other users.

        .. include:: /_includes/usable-by/users-bots.rst

        Returns:
            List of :obj:`~pyrogram.types.Gift` | :obj:`~pyrogram.types.UpgradedGift`: On success, a list of star gifts that can be sent by the Client to users and channel chats is returned.

        Example:
            .. code-block:: python

                app.get_available_gifts()
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGifts(hash=0)
        )

        return types.List([
            await types.Gift._parse(self, gift, {})
            for gift in r.gifts
        ])
