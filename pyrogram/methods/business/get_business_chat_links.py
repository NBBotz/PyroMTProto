#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class GetBusinessChatLinks:
    async def get_business_chat_links(
        self: "pyrogram.Client",
    ) -> list:
        """Get all your Business chat links.

        Business chat links are special deep-links that open a chat
        with your Business account and optionally pre-fill a message.

        Returns:
            ``list`` of :obj:`~pyrogram.raw.types.account.BusinessChatLinks`.

        Example:
            .. code-block:: python

                links = await app.get_business_chat_links()
                for link in links.links:
                    print(link.link, link.title)
        """
        return await self.invoke(
            raw.functions.account.GetBusinessChatLinks()
        )
