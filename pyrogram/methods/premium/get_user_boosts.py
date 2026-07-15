#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class GetUserBoosts:
    async def get_user_boosts(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
    ):
        """Get boost slots a specific user has applied to a channel.

        Parameters:
            chat_id (``int`` | ``str``):
                The channel or group to check.

            user_id (``int`` | ``str``):
                The user whose boosts to retrieve.

        Returns:
            :obj:`~pyrogram.raw.types.premium.BoostsList` with the boosts
            this user has applied to the specified channel.

        Example:
            .. code-block:: python

                boosts = await app.get_user_boosts("@channel", "username")
                print(f"User applied {len(boosts.boosts)} boosts")
        """
        peer = await self.resolve_peer(chat_id)
        user = await self.resolve_peer(user_id)
        return await self.invoke(
            raw.functions.premium.GetUserBoosts(peer=peer, user_id=user)
        )
