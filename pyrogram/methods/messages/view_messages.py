#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw


class ViewMessages:
    async def view_messages(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_ids: Union[int, list[int]],
        force_read: bool = True
    ) -> bool:
        """Informs the server that messages are being viewed by the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_ids (``int`` | List of ``int``):
                Identifier or list of message identifiers of the target message.

            force_read (``bool``, *optional*):
                Pass True to mark as read the specified messages and also increment the view counter.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Increment message views
                await app.view_messages(chat_id, 1)
        """
        ids = [message_ids] if not isinstance(message_ids, list) else message_ids

        r = await self.invoke(
            raw.functions.messages.GetMessagesViews(
                peer=await self.resolve_peer(chat_id),
                id=ids,
                increment=force_read
            )
        )

        return bool(r)
