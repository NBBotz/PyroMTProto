#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw
from pyrogram import types


class CreateChannel:
    async def create_channel(
        self: "pyrogram.Client",
        title: str,
        description: str = "",
        message_auto_delete_time: int = 0
    ) -> "types.Chat":
        """Create a new broadcast channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            title (``str``):
                The channel title.

            description (``str``, *optional*):
                The channel description.

            message_auto_delete_time (``int``, *optional*):
                Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically.

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                await app.create_channel("Channel Title", "Channel Description")
        """
        r = await self.invoke(
            raw.functions.channels.CreateChannel(
                title=title,
                about=description,
                broadcast=True,
                ttl_period=message_auto_delete_time
            )
        )

        return types.Chat._parse_chat(self, r.chats[0])
