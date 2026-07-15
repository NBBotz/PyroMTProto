#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class CountPublicMessagesByTag:
    async def count_public_messages_by_tag(
        self: "pyrogram.Client",
        tag: str = "",
    ) -> int:
        """Get the count of messages with the provided hashtag or cashtag.

        If you want to get the actual messages, see :meth:`~pyrogram.Client.search_public_messages_by_tag`.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            hashtag (``str``, *optional*):
                Hashtag or cashtag to search for.

        Returns:
            ``int``: On success, the messages count is returned.

        """
        r = await self.invoke(
            raw.functions.channels.SearchPosts(
                hashtag=tag,
                offset_rate=0,
                offset_peer=raw.types.InputPeerEmpty(),
                offset_id=0,
                limit=1
            )
        )

        if hasattr(r, "count"):
            return r.count
        else:
            return len(r.messages)
