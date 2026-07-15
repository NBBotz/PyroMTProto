#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import logging

import pyrogram
from pyrogram import raw
from pyrogram import types

log = logging.getLogger(__name__)


class RecoverPassword:
    async def recover_password(
        self: "pyrogram.Client",
        recovery_code: str
    ) -> "types.User":
        """Recover your password with a recovery code and log in.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            recovery_code (``str``):
                The recovery code sent via email.

        Returns:
            :obj:`~pyrogram.types.User`: On success, the authorized user is returned and the Two-Step Verification
            password reset.

        Raises:
            BadRequest: In case the recovery code is invalid.
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        """
        r = await self.invoke(
            raw.functions.auth.RecoverPassword(
                code=recovery_code
            )
        )

        await self.storage.user_id(r.user.id)
        await self.storage.is_bot(False)

        return types.User._parse(self, r.user)
