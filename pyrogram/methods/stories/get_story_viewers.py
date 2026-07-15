#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional, AsyncGenerator
import pyrogram
from pyrogram import raw


class GetStoryViewers:
    async def get_story_viewers(
        self: "pyrogram.Client",
        story_id: int,
        chat_id: Union[int, str] = "me",
        query: Optional[str] = None,
        reactions_first: bool = False,
        forwards_first: bool = False,
        offset: str = "",
        limit: int = 100,
    ) -> AsyncGenerator:
        """Get the list of viewers for one of your stories.

        Parameters:
            story_id (``int``):
                ID of the story to get viewers for.

            chat_id (``int`` | ``str``, *optional*):
                The story owner's ID. Defaults to ``"me"`` (your stories).

            query (``str``, *optional*):
                Search filter — only return viewers whose name matches.

            reactions_first (``bool``, *optional*):
                If True, show viewers who reacted first.

            forwards_first (``bool``, *optional*):
                If True, show viewers who forwarded the story first.

            offset (``str``, *optional*):
                Pagination offset.

            limit (``int``, *optional*):
                Maximum viewers to fetch. Defaults to 100.

        Yields:
            :obj:`~pyrogram.raw.types.StoryView` for each viewer.

        Example:
            .. code-block:: python

                async for viewer in app.get_story_viewers(story_id=5):
                    print(viewer.user_id)
        """
        peer = await self.resolve_peer(chat_id)

        while True:
            r = await self.invoke(
                raw.functions.stories.GetStoryViewsList(
                    peer=peer,
                    id=story_id,
                    q=query,
                    reactions_first=reactions_first,
                    forwards_first=forwards_first,
                    offset=offset,
                    limit=min(limit, 100),
                )
            )

            for view in r.views:
                yield view
                limit -= 1
                if limit == 0:
                    return

            if not r.next_offset:
                break
            offset = r.next_offset
