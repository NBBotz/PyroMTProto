#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class CreateGroup:
    async def create_group(
        self: "pyrogram.Client",
        title: str,
        users: Union[Union[int, str], list[Union[int, str]]] = None,
        message_auto_delete_time: int = 0
    ) -> "types.Chat":
        """Create a new basic group.

        .. note::

            If you want to create a new supergroup, use :meth:`~pyrogram.Client.create_supergroup` instead.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            title (``str``):
                The group title.

            users (``int`` | ``str`` | List of ``int`` or ``str``):
                Users to create a chat with.
                Multiple users can be invited by passing a list of IDs, usernames or phone numbers.
                Identifiers of users to be added to the basic group; may be empty to create a basic group without other members
            
            message_auto_delete_time (``int``, *optional*):
                Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically.

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                await app.create_group("Group Title", user_id)
        """
        if users and not isinstance(users, list):
            users = [users]
        r = await self.invoke(
            raw.functions.messages.CreateChat(
                users=[await self.resolve_peer(u) for u in users] if users else [],
                title=title,
                ttl_period=message_auto_delete_time
            )
        )
        return types.Chat._parse_chat(self, r.updates.chats[0])
