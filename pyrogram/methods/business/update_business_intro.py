#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union, TYPE_CHECKING
import pyrogram
from pyrogram import raw

if TYPE_CHECKING:
    pass


class UpdateBusinessIntro:
    async def update_business_intro(
        self: "pyrogram.Client",
        title: Optional[str] = None,
        description: Optional[str] = None,
        sticker: Optional["pyrogram.types.InputMedia"] = None,
    ) -> bool:
        """Update the intro displayed on your Telegram Business profile.

        The business intro is shown to users who open your profile
        before they have sent you any messages.

        Parameters:
            title (``str``, *optional*):
                Intro title. Pass None or empty string to clear.

            description (``str``, *optional*):
                Intro description text. Pass None or empty string to clear.

            sticker (``InputMedia``, *optional*):
                A sticker to display alongside the intro. Pass None to remove.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.update_business_intro(
                    title="Welcome!",
                    description="I usually reply within a few hours."
                )

                # Clear the intro completely
                await app.update_business_intro()
        """
        intro = None
        if title is not None or description is not None or sticker is not None:
            sticker_doc = None
            if sticker is not None:
                media = await self.resolve_peer(sticker) if isinstance(sticker, str) else None
                # Accept an InputDocument directly
                sticker_doc = sticker if isinstance(sticker, raw.types.InputDocument) else None

            intro = raw.types.BusinessIntro(
                title=title or "",
                description=description or "",
                sticker=sticker_doc,
            )

        await self.invoke(
            raw.functions.account.UpdateBusinessIntro(intro=intro)
        )
        return True
