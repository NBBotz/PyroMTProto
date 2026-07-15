#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class DeleteBusinessChatLink:
    async def delete_business_chat_link(
        self: "pyrogram.Client",
        slug: str,
    ) -> bool:
        """Delete a Business chat link.

        Parameters:
            slug (``str``):
                The unique slug of the link to delete (last part of the link URL,
                e.g. ``"abcXYZ123"`` from ``"https://t.me/m/abcXYZ123"``).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_business_chat_link("abcXYZ123")
        """
        await self.invoke(
            raw.functions.account.DeleteBusinessChatLink(slug=slug)
        )
        return True
