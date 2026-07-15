#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetBotDefaultPrivileges:
    async def get_bot_default_privileges(
        self: "pyrogram.Client",
        for_channels: bool = None
    ) -> Optional["types.ChatPrivileges"]:
        """Get the current default privileges of the bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            for_channels (``bool``, *optional*):
                Pass True to get default privileges of the bot in channels. Otherwise, default privileges of the bot
                for groups and supergroups will be returned.

        Returns:
            ``bool``: On success, True is returned.

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        Example:
            .. code-block:: python

                privileges = await app.get_bot_default_privileges()
        """

        bot_info = await self.invoke(
            raw.functions.users.GetFullUser(
                id=raw.types.InputUserSelf()
            )
        )

        field = "bot_broadcast_admin_rights" if for_channels else "bot_group_admin_rights"

        admin_rights = getattr(bot_info.full_user, field)

        return types.ChatPrivileges._parse(admin_rights) if admin_rights else None
