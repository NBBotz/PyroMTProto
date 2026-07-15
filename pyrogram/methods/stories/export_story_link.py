#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class ExportStoryLink:
    async def export_story_link(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
    ) -> str:
        """Get a shareable link for a story.

        Parameters:
            chat_id (``int`` | ``str``):
                Owner of the story.

            story_id (``int``):
                ID of the story.

        Returns:
            ``str``: The story's shareable URL (e.g. ``"https://t.me/c/123456/s/1"``).

        Example:
            .. code-block:: python

                link = await app.export_story_link("@channel", story_id=5)
                print(link)
        """
        peer = await self.resolve_peer(chat_id)
        r = await self.invoke(
            raw.functions.stories.ExportStoryLink(
                peer=peer,
                id=story_id,
            )
        )
        return r.link
