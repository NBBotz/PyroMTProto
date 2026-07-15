#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class ResolveBusinessChatLink:
    async def resolve_business_chat_link(
        self: "pyrogram.Client",
        slug: str,
    ):
        """Resolve a Business chat link and get its details.

        Parameters:
            slug (``str``):
                The slug/username part of the business link.

        Returns:
            :obj:`~pyrogram.raw.types.account.ResolvedBusinessChatLinks` with
            ``peer``, ``message``, and ``entities`` fields.

        Example:
            .. code-block:: python

                result = await app.resolve_business_chat_link("abcXYZ123")
                print(result.message)
        """
        return await self.invoke(
            raw.functions.account.ResolveBusinessChatLink(slug=slug)
        )
