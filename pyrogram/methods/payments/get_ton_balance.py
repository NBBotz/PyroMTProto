#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw


class GetTonBalance:
    async def get_ton_balance(
        self: "pyrogram.Client"
    ) -> float:
        """Get the current TON balance of the current account.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            ``float``: On success, the current stars balance is returned.

        Example:
            .. code-block:: python

                # Get stars balance of current account
                await app.get_stars_balance()

                # Get stars balance of a bot
                await app.get_stars_balance(chat_id="pyrogrambot")
        """
        r = await self.invoke(
            raw.functions.payments.GetStarsTransactions(
                peer=raw.types.InputPeerSelf(),
                offset="",
                limit=0,
                ton=True
            )
        )

        return r.balance.amount

