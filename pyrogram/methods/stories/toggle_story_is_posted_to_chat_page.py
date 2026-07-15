#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Iterable

import pyrogram
from pyrogram import raw, types, utils


class ToggleStoryIsPostedToChatPage:
    async def toggle_story_is_posted_to_chat_page(
        self: "pyrogram.Client",
        story_poster_chat_id: Union[int, str],
        story_ids: Union[int, Iterable[int]],
        is_posted_to_chat_page: bool = True,
    ) -> list[int]:
        """Toggles whether a story is accessible after expiration.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            story_poster_chat_id (``int`` | ``str``):
                Identifier of the chat that posted the story.
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            story_ids (``int`` | Iterable of ``int``):
                List of identifiers of the target stories.
            
            is_posted_to_chat_page (``bool``, *optional*):
                Pass True to make the story accessible after expiration; pass False to make it private.

        Returns:
            List of ``int``: List of updated story IDs.

        Example:
            .. code-block:: python

                # Pin a single story
                await app.toggle_story_is_posted_to_chat_page(story_poster_chat_id, story_id)

        """
        is_iterable = utils.is_list_like(story_ids)
        story_ids = list(story_ids) if is_iterable else [story_ids]

        r = await self.invoke(
            raw.functions.stories.TogglePinned(
                peer=await self.resolve_peer(story_poster_chat_id),
                id=story_ids,
                pinned=is_posted_to_chat_page
            )
        )

        return types.List(r)
