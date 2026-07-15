#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional

import pyrogram
from pyrogram import raw


class SetSlowMode:
    async def set_slow_mode(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        seconds: Optional[int]
    ) -> bool:
        """Set the slow mode interval for a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            seconds (``int`` | ``None``):
                New slow mode delay for the chat, in seconds; must be one of: 0 or None (off), 5, 10, 30, 60 (1 minute), 300 (5 minutes), 900 (15 minutes), 3600 (1 hour).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Set slow mode to 60 seconds
                await app.set_slow_mode(chat_id, 60)

                # Disable slow mode
                await app.set_slow_mode(chat_id, None)
        """

        await self.invoke(
            raw.functions.channels.ToggleSlowMode(
                channel=await self.resolve_peer(chat_id),
                seconds=seconds or 0
            )
        )

        return True
