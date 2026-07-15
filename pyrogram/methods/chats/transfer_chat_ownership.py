#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram.utils import compute_password_check


class TransferChatOwnership:
    async def transfer_chat_ownership(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
        password: str,
    ) -> bool:
        """Changes the owner of a chat.
        
        Requires owner privileges in the chat. Available only for supergroups and channel chats.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the new owner.
                The ownership can't be transferred to a bot or to a deleted user.

            password (``str``):
                The 2-step verification password of the current user.

        Returns:
            ``bool``: True on success.

        Raises:
            ValueError: In case of invalid parameters.
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        Example:
            .. code-block:: python

                await app.transfer_chat_ownership(chat_id, user_id, "password")
        """

        peer_channel = await self.resolve_peer(chat_id)
        peer_user = await self.resolve_peer(user_id)

        if not isinstance(peer_channel, raw.types.InputPeerChannel):
            raise ValueError("The chat_id must belong to a channel/supergroup.")

        if not isinstance(peer_user, raw.types.InputPeerUser):
            raise ValueError("The user_id must belong to a user.")

        r = await self.invoke(
            raw.functions.channels.EditCreator(
                channel=peer_channel,
                user_id=peer_user,
                password=compute_password_check(
                    await self.invoke(raw.functions.account.GetPassword()), password
                ),
            )
        )

        return bool(r)
