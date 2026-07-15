#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import types, raw


class DiscardGroupCall:
    async def discard_group_call(
        # TODO
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> "types.Message":
        """Terminate a group/channel call or livestream

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat. A chat can be either a basic group, supergroup or a channel.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent service message is returned.

        Example:
            .. code-block:: python

                await app.discard_group_call(chat_id)

        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChannel):
            r = await self.invoke(raw.functions.channels.GetFullChannel(channel=peer))
        elif isinstance(peer, raw.types.InputPeerChat):
            r = await self.invoke(
                raw.functions.messages.GetFullChat(chat_id=peer.chat_id)
            )
        else:
            raise ValueError("Target chat should be group, supergroup or channel.")

        call = r.full_chat.call

        if call is None:
            raise ValueError("No active group call at this chat.")

        r = await self.invoke(
            raw.functions.phone.DiscardGroupCall(
                call=call
            )
        )

        for i in r.updates:
            if isinstance(
                i,
                (
                    raw.types.UpdateNewChannelMessage,
                    raw.types.UpdateNewMessage,
                    raw.types.UpdateNewScheduledMessage,
                ),
            ):
                return await types.Message._parse(
                    self,
                    i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage),
                )
