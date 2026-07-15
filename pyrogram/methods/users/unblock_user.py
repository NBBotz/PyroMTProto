#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw


class UnblockUser:
    async def unblock_user(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        my_stories_from: bool = None
    ) -> bool:
        """Unblock a user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            my_stories_from (``bool``, *optional*):
                Whether the peer should be removed from the story blocklist; if not set, the peer will be removed from the main blocklist.

        Returns:
            ``bool``: True on success

        Example:
            .. code-block:: python

                await app.unblock_user(user_id)
        """
        return bool(
            await self.invoke(
                raw.functions.contacts.Unblock(
                    id=await self.resolve_peer(user_id),
                    my_stories_from=my_stories_from
                )
            )
        )
