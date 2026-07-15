#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw


class BlockUser:
    async def block_user(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        my_stories_from: bool = None
    ) -> bool:
        """Block a user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use their phone number (str).

            my_stories_from (``bool``, *optional*):
                Whether the peer should be added to the story blocklist; if not set, the peer will be added to the main blocklist.

        Returns:
            ``bool``: True on success

        Example:
            .. code-block:: python

                await app.block_user(user_id)
        """
        return bool(
            await self.invoke(
                raw.functions.contacts.Block(
                    id=await self.resolve_peer(user_id),
                    my_stories_from=my_stories_from
                )
            )
        )
