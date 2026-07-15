#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class GetAccountTTL:
    async def get_account_ttl(
        self: "pyrogram.Client",
    ):
        """Get days to live of account.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            ``int``: Time to live in days of the current account.

        Example:
            .. code-block:: python

                # Get ttl in days
                await app.get_account_ttl()
        """
        r = await self.invoke(
            raw.functions.account.GetAccountTTL()
        )

        return r.days

