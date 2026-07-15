#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class UpdateStatus:
    async def update_status(
        self: "pyrogram.Client",
        offline: bool = False,
    ) -> bool:
        """Updates online user status.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            offline (``bool``):
                If (True) is transmitted, user status will change to (UserStatusOffline), Otherwise user status will change to (UserStatusOnline).

        Returns:
            `bool`: True On success.

        Example:
            .. code-block:: python

                await app.update_status()
        """
        r = await self.invoke(raw.functions.account.UpdateStatus(offline=offline))

        return bool(r)
