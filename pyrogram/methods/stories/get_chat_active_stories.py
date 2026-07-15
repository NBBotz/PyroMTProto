#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from asyncio import sleep
from typing import AsyncGenerator, Union

import pyrogram
from pyrogram import raw, types


class GetChatActiveStories:
    async def get_chat_active_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> AsyncGenerator["types.Story", None]:
        """Get all non expired stories from a chat by using chat identifier.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For your personal story you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.Story` objects is returned.

        Example:
            .. code-block:: python

                # Get all non expired stories from specific chat
                async for story in app.get_chat_active_stories(chat_id):
                    print(story)

        Raises:
            ValueError: In case of invalid arguments.

        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.stories.GetPeerStories(
                peer=peer
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}
        peer = r.stories.peer

        for story in r.stories.stories:
            await sleep(0)
            yield await types.Story._parse(
                self,
                users,
                chats,
                None, None, None,
                story,
                peer
            )
