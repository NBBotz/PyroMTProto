#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types


class GetActiveSessions:
    async def get_active_sessions(
        self: "pyrogram.Client"
    ) -> "types.ActiveSessions":
        """Returns all active sessions of the current user.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.types.ActiveSessions`: On success, all the active sessions of the current user is returned.

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        """
        r = await self.invoke(
            raw.functions.account.GetAuthorizations()
        )
        return types.ActiveSessions._parse(self, r)
