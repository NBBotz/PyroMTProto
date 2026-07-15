#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw
from typing import Union


class ToggleForumTopicIsPinned:
    async def toggle_forum_topic_is_pinned(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_thread_id: int,
        is_pinned: bool
    ) -> bool:
        """Changes the pinned state of a forum topic; requires can_manage_topics right in the supergroup. There can be up to ``pinned_forum_topic_count_max`` pinned forum topics.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_thread_id (``int``):
                Unique identifier for the target message thread of the forum topic.

            is_pinned (``bool``):
                Pass True to pin the topic; pass False to unpin it.

        Returns:
            ``bool``: On success, True is returned.

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        Example:
            .. code-block:: python

                await app.toggle_forum_topic_is_pinned(chat_id, topic_id, True)
        """
        await self.invoke(
            raw.functions.messages.UpdatePinnedForumTopic(
                peer=await self.resolve_peer(chat_id),
                topic_id=message_thread_id,
                pinned=is_pinned
            )
        )
        # TODO
        return True
