#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class IncrementStoryViews:
    async def increment_story_views(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_ids: list[int],
    ) -> bool:
        """Mark stories as viewed (increment view counters).

        Call this after fetching and displaying stories to the user so that
        Telegram records the views correctly.

        Parameters:
            chat_id (``int`` | ``str``):
                The peer whose stories were viewed.

            story_ids (``list`` of ``int``):
                IDs of the stories that were viewed (up to 200 at once).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.increment_story_views("@channel", [1, 2, 3])
        """
        peer = await self.resolve_peer(chat_id)
        await self.invoke(
            raw.functions.stories.IncrementStoryViews(
                peer=peer,
                id=story_ids[:200],
            )
        )
        return True
