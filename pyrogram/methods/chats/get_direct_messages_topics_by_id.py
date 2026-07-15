#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import logging
from typing import Iterable, Union

import pyrogram
from pyrogram import raw, types, utils

log = logging.getLogger(__name__)


class GetDirectMessagesTopicsByID:
    async def get_direct_messages_topics_by_id(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_ids: Union[int, Iterable[int]]
    ) -> Union[
        "types.DirectMessagesTopic",
        list["types.DirectMessagesTopic"]
    ]:
        """Get one or more direct message topic from a chat by using topic identifiers.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            topic_ids (``int`` | Iterable of ``int``, *optional*):
                Pass a single topic identifier or an iterable of topic ids (as integers) to get the information of the
                topic themselves.

        Returns:
            :obj:`~pyrogram.types.DirectMessagesTopic` | List of :obj:`~pyrogram.types.DirectMessagesTopic`: In case *topic_ids* was not
            a list, a single topic is returned, otherwise a list of topics is returned.

        Example:
            .. code-block:: python

                # Get one topic
                await app.get_direct_messages_topics_by_id(chat_id, 12345)

                # Get more than one topic (list of topics)
                await app.get_direct_messages_topics_by_id(chat_id, [12345, 12346])

        """

        is_iterable = utils.is_list_like(topic_ids)
        ids = list(topic_ids) if is_iterable else [topic_ids]

        r = await self.invoke(
            raw.functions.messages.GetSavedDialogsByID(
                ids=[await self.resolve_peer(i) for i in ids],
                parent_peer=await self.resolve_peer(chat_id)
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        topics = types.List()

        for i in r.dialogs:
            topics.append(
                types.DirectMessagesTopic._parse_dialog(
                    client=self,
                    topic=i,
                    users=users,
                    chats=chats
                )
            )

        return topics if is_iterable else topics[0] if topics else None
