#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram
from pyrogram import raw, utils
from pyrogram import types
from ..object import Object
from ..update import Update


class ChatJoinRequest(Object, Update):
    """Represents a join request sent to a chat.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            Chat to which the request was sent.

        from_user (:obj:`~pyrogram.types.User`):
            User that sent the join request.

        user_chat_id (``int``):
            Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user.

        date (:py:obj:`~datetime.datetime`):
            Date the request was sent.

        bio (``str``, *optional*):
            Bio of the user.

        invite_link (:obj:`~pyrogram.types.ChatInviteLink`, *optional*):
            Chat invite link that was used by the user to send the join request.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chat: "types.Chat",
        from_user: "types.User",
        user_chat_id: int,
        date: datetime,
        bio: str = None,
        invite_link: "types.ChatInviteLink" = None
    ):
        super().__init__(client)

        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        update: "raw.types.UpdateBotChatInviteRequester",
        users: dict[int, "raw.types.User"],
        chats: dict[int, "raw.types.Chat"]
    ) -> "ChatJoinRequest":
        chat_id = utils.get_raw_peer_id(update.peer)
        return ChatJoinRequest(
            chat=types.Chat._parse_chat(client, chats[chat_id]),
            from_user=types.User._parse(client, users[update.user_id]),
            user_chat_id=update.user_id,  # TODO
            date=utils.timestamp_to_datetime(update.date),
            bio=update.about,
            invite_link=types.ChatInviteLink._parse(client, update.invite, users),
            client=client
        )

    async def approve(self) -> bool:
        """Bound method *approve* of :obj:`~pyrogram.types.ChatJoinRequest`.
        
        Use as a shortcut for:
        
        .. code-block:: python

            await client.approve_chat_join_request(
                chat_id=request.chat.id,
                user_id=request.from_user.id
            )
            
        Example:
            .. code-block:: python

                await request.approve()
                
        Returns:
            ``bool``: True on success.
        
        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        """
        return await self._client.approve_chat_join_request(
            chat_id=self.chat.id,
            user_id=self.from_user.id
        )

    async def decline(self) -> bool:
        """Bound method *decline* of :obj:`~pyrogram.types.ChatJoinRequest`.
        
        Use as a shortcut for:
        
        .. code-block:: python

            await client.decline_chat_join_request(
                chat_id=request.chat.id,
                user_id=request.from_user.id
            )
            
        Example:
            .. code-block:: python

                await request.decline()
                
        Returns:
            ``bool``: True on success.
        
        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        """
        return await self._client.decline_chat_join_request(
            chat_id=self.chat.id,
            user_id=self.from_user.id
        )

    # TODO
