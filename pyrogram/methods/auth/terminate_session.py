#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class TerminateSession:
    async def terminate_session(
        self: "pyrogram.Client",
        session_id: int
    ) -> bool:
        """Terminates a session of the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            session_id (``int``):
                Session identifier.

        Returns:
            ``bool``: On success, in case the session is destroyed, True is returned. Otherwise, False is returned.

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        """
        return await self.invoke(
            raw.functions.account.ResetAuthorization(hash=session_id)
        )
