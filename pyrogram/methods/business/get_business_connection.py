#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import types, utils, raw


class GetBusinessConnection:
    async def get_business_connection(
        self: "pyrogram.Client",
        business_connection_id: str
    ) -> "types.Message":
        """Use this method to get information about the connection of the bot with a business account.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection

        Returns:
            :obj:`~pyrogram.types.BusinessConnection`: On success, the the connection of the bot with a business account is returned.
        """

        r = await self.invoke(
            raw.functions.account.GetBotBusinessConnection(
                connection_id=business_connection_id
            )
        )
        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}
        for i in r.updates:
            if isinstance(
                i,
                (
                    raw.types.UpdateBotBusinessConnect
                )
            ):
                business_connection = types.BusinessConnection._parse(
                    self,
                    i,
                    users,
                    chats
                )
                self.business_user_connection_cache[
                    business_connection_id
                ] = business_connection
                return business_connection
