#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types


class ActivateStealthMode:
    async def activate_stealth_mode(
        self: "pyrogram.Client",
        past: bool = True,
        future: bool = True,
    ) -> "types.StoryStealthMode":
        """Activate Stories Stealth Mode (Premium feature).

        When stealth mode is active, Telegram will not record your views
        on other users' stories.

        Parameters:
            past (``bool``, *optional*):
                If True, hide views on stories you already viewed in the
                past 5 minutes. Defaults to True.

            future (``bool``, *optional*):
                If True, hide views for the next 25 minutes.
                Defaults to True.

        Returns:
            :obj:`~pyrogram.types.StoryStealthMode` with the updated
            stealth mode state (``active_until_date``, ``cooldown_until_date``).

        Example:
            .. code-block:: python

                mode = await app.activate_stealth_mode()
                print(f"Stealth active until {mode.active_until_date}")
        """
        r = await self.invoke(
            raw.functions.stories.ActivateStealthMode(
                past=past,
                future=future,
            )
        )

        # r.updates contains UpdateStoriesStealthMode
        for update in getattr(r, "updates", []):
            if isinstance(update, raw.types.UpdateStoriesStealthMode):
                return types.StoryStealthMode._parse(update.stealth_mode)

        return types.StoryStealthMode._parse(None)
