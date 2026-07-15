#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw, types


class HideMyStoryView:
    async def hide_my_story_view(
        self: "pyrogram.Client",
        past: Optional[bool] = True,
        future: Optional[bool] = True,
    ) -> Union["types.StoryStealthMode", bool]:
        """Activates stealth mode for stories, which hides all views of stories from the current user in the last "stories_stealth_past_period" seconds and for the next "stories_stealth_future_period" seconds; for Telegram Premium users only.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            past (``bool``, *optional*):
                Pass True to erase views from any stories opened in the past stories_stealth_past_period seconds, as specified by the client configuration.

            future (``bool``, *optional*):
                Pass True to hide future story views for the next stories_stealth_future_period seconds, as specified by the client configuration.

        Returns:
            :obj:`~pyrogram.types.StoryStealthMode`: On success, the information about stealth mode session is returned.

        Example:
            .. code-block:: python

                # Erase and hide story views in the past stories_stealth_past_period and the next stories_stealth_future_period seconds
                await app.hide_my_story_view()

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        """

        r = await self.invoke(
            raw.functions.stories.ActivateStealthMode(
                past=past,
                future=future
            )
        )
        for i in r.updates:
            if isinstance(i, raw.types.UpdateStoriesStealthMode):
                return types.StoryStealthMode._parse(i.stealth_mode)
        return False
