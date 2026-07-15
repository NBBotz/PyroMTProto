#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types


class GetGlobalPrivacySettings:
    async def get_global_privacy_settings(self: "pyrogram.Client") -> "types.GlobalPrivacySettings":
        """Get account global privacy settings.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.types.GlobalPrivacySettings`: On success, the global privacy settings is returned.

        Example:
            .. code-block:: python

                await app.get_global_privacy_settings()
        """
        r = await self.invoke(raw.functions.account.GetGlobalPrivacySettings())

        return types.GlobalPrivacySettings._parse(r)

