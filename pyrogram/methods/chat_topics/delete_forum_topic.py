#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import types, utils, raw


class DeleteForumTopic:
    async def delete_forum_topic(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> int:
        """Use this method to delete a forum topic along with all its messages in a forum supergroup chat or a private chat with a user.
        
        In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the ``can_delete_messages`` administrator rights

        unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_thread_id (``int``):
                Unique identifier for the target message thread of the forum topic

        Returns:
            ``int``: Amount of affected messages

        Example:
            .. code-block:: python

                # Create a new Topic
                message = await app.create_forum_topic(chat, "Topic Title")
                # Delete the Topic
                await app.delete_forum_topic(chat, message.id)
        """

        r = await self.invoke(
            raw.functions.messages.DeleteTopicHistory(
                peer=await self.resolve_peer(chat_id),
                top_msg_id=message_thread_id
            )
        )
        return r.pts_count
