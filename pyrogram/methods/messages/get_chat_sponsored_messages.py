#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw, types


class GetChatSponsoredMessages:
    async def get_chat_sponsored_messages(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> Optional[list["types.SponsoredMessage"]]:
        """Returns sponsored messages to be shown in a chat; for channel chats only.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            List of :obj:`~pyrogram.types.SponsoredMessage`: a list of sponsored messages is returned.

        Example:
            .. code-block:: python

                # Get a sponsored messages
                sm = await app.get_chat_sponsored_messages(chat_id)
                print(sm)

        """
        r = await self.invoke(
            raw.functions.messages.GetSponsoredMessages(
                peer=await self.resolve_peer(chat_id)
            )
        )

        if isinstance(r, raw.types.messages.SponsoredMessagesEmpty):
            return None

        return types.List([
            types.SponsoredMessage._parse(self, sm)
            for sm in r.messages
        ])
