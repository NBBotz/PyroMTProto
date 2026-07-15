#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw, types


class GetSendAsChats:
    async def get_send_as_chats(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        for_paid_reactions: Optional[bool] = None,
        for_live_stories: Optional[bool] = None,
    ) -> list["types.Chat"]:
        """Get the list of "send_as" chats available.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            for_paid_reactions (``bool``, *optional*):
                Pass True to get the list of available send_as chats for paid reactions.

            for_live_stories (``bool``, *optional*):
                Pass True to get the list of available send_as chats for viewing live stories.

        Returns:
            List of :obj:`~pyrogram.types.Chat`: The list of chats.

        Example:
            .. code-block:: python

                chats = await app.get_send_as_chats(chat_id)
                print(chats)

        """
        r = await self.invoke(
            raw.functions.channels.GetSendAs(
                peer=await self.resolve_peer(chat_id),
                for_paid_reactions=for_paid_reactions,
                for_live_stories=for_live_stories
            )
        )

        users = {u.id: u for u in r.users}
        chats = {c.id: c for c in r.chats}

        send_as_chats = types.List()

        for p in r.peers:
            # TODO
            if isinstance(p.peer, raw.types.PeerUser):
                send_as_chats.append(types.Chat._parse_chat(self, users[p.peer.user_id]))
            else:
                send_as_chats.append(types.Chat._parse_chat(self, chats[p.peer.channel_id]))

        return send_as_chats
