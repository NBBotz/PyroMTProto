#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional
import pyrogram
from pyrogram import raw


class EditBusinessChatLink:
    async def edit_business_chat_link(
        self: "pyrogram.Client",
        slug: str,
        text: Optional[str] = None,
        title: Optional[str] = None,
    ):
        """Edit an existing Business chat link.

        Parameters:
            slug (``str``):
                Unique slug of the link to edit.

            text (``str``, *optional*):
                New pre-filled message text.

            title (``str``, *optional*):
                New internal title.

        Returns:
            :obj:`~pyrogram.raw.types.account.BusinessChatLink` on success.
        """
        link_data = raw.types.InputBusinessChatLink(
            message=text or "",
            title=title,
        )
        return await self.invoke(
            raw.functions.account.EditBusinessChatLink(slug=slug, link=link_data)
        )
