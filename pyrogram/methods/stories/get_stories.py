#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Iterable

import pyrogram
from pyrogram import raw, types, utils


class GetStories:
    async def get_stories(
        self: "pyrogram.Client",
        story_poster_chat_id: Union[int, str],
        story_ids: Union[int, Iterable[int]],
    ) -> Union["types.Story", list["types.Story"]] :
        """Get one or more stories from a chat by using stories identifiers.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            story_poster_chat_id (``int`` | ``str``):
                Identifier of the chat that posted the story.

            story_ids (``int`` | Iterable of ``int``, *optional*):
                Pass a single story identifier or an iterable of story ids (as integers) to get the content of the
                story themselves.

        Returns:
            :obj:`~pyrogram.types.Story` | List of :obj:`~pyrogram.types.Story`: In case *story_ids* was not
            a list, a single story is returned, otherwise a list of stories is returned.

        Example:
            .. code-block:: python

                # Get stories by id
                stories = await app.get_stories(
                    story_poster_chat_id,
                    [1, 2, 3]
                )

                for story in stories:
                    print(story)
        """

        is_iterable = utils.is_list_like(story_ids)
        ids = list(story_ids) if is_iterable else [story_ids]

        peer = await self.resolve_peer(story_poster_chat_id)
        r = await self.invoke(
            raw.functions.stories.GetStoriesByID(
                peer=peer,
                id=ids
            )
        )

        stories = []

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for story in r.stories:
            stories.append(
                await types.Story._parse(
                    self,
                    users,
                    chats,
                    None, None, None,
                    # TODO
                    story,
                    None, #
                    # TODO
                )
            )

        return types.List(stories) if is_iterable else stories[0] if stories else None
