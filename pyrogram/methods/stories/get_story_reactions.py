#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional, AsyncGenerator
import pyrogram
from pyrogram import raw


class GetStoryReactions:
    async def get_story_reactions(
        self: "pyrogram.Client",
        story_id: int,
        chat_id: Union[int, str] = "me",
        reaction: Optional[str] = None,
        offset: str = "",
        limit: int = 100,
    ) -> AsyncGenerator:
        """Get users who reacted to one of your stories.

        Parameters:
            story_id (``int``):
                ID of the story to inspect.

            chat_id (``int`` | ``str``, *optional*):
                Story owner. Defaults to ``"me"``.

            reaction (``str``, *optional*):
                Filter by a specific reaction emoji (e.g. ``"❤️"``).
                Omit to get all reactions.

            offset (``str``, *optional*):
                Pagination offset.

            limit (``int``, *optional*):
                Maximum number of reactors. Defaults to 100.

        Yields:
            :obj:`~pyrogram.raw.types.StoryReaction` for each reactor.

        Example:
            .. code-block:: python

                async for reaction in app.get_story_reactions(story_id=5):
                    print(reaction.peer_id)
        """
        peer = await self.resolve_peer(chat_id)
        raw_reaction = raw.types.ReactionEmoji(emoticon=reaction) if reaction else None

        while True:
            r = await self.invoke(
                raw.functions.stories.GetStoryReactionsList(
                    peer=peer,
                    id=story_id,
                    reaction=raw_reaction,
                    offset=offset,
                    limit=min(limit, 100),
                )
            )

            for item in r.reactions:
                yield item
                limit -= 1
                if limit == 0:
                    return

            if not r.next_offset:
                break
            offset = r.next_offset
