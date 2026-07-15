#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw


class UnpinAllChatMessages:
    async def unpin_all_chat_messages(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_thread_id: int = None
    ) -> int:
        """
        Use this method to clear the list of pinned messages in a chat.
        If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have
        the 'can_pin_messages' admin right in a supergroup or 'can_edit_messages' admin right in a channel.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread of the forum topic.

        Returns:
            ``int``: Amount of affected messages

        Example:
            .. code-block:: python

                # Unpin all chat messages
                await app.unpin_all_chat_messages(chat_id)
        """
        r = await self.invoke(
            raw.functions.messages.UnpinAllMessages(
                peer=await self.resolve_peer(chat_id),
                top_msg_id=message_thread_id
            )
        )
        return r.pts_count
