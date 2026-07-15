#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional
import pyrogram
from pyrogram import raw


class CreateBusinessChatLink:
    async def create_business_chat_link(
        self: "pyrogram.Client",
        text: Optional[str] = None,
        title: Optional[str] = None,
    ):
        """Create a new Business chat link.

        Parameters:
            text (``str``, *optional*):
                Pre-filled message text that appears in the message input
                when the user opens the link.

            title (``str``, *optional*):
                Internal title for this link (only visible to you).

        Returns:
            :obj:`~pyrogram.raw.types.account.BusinessChatLink` on success.

        Example:
            .. code-block:: python

                link = await app.create_business_chat_link(
                    text="Hello! I'd like to place an order.",
                    title="Order link"
                )
                print(link.link)
        """
        link_data = raw.types.InputBusinessChatLink(
            message=text or "",
            title=title,
        )
        return await self.invoke(
            raw.functions.account.CreateBusinessChatLink(link=link_data)
        )
