#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw


class SetPersonalChat:
    async def set_personal_chat(
        self: "pyrogram.Client",
        chat_id: Optional[Union[int, str]] = None,
    ) -> bool:
        """Changes the personal chat of the current user

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Identifier of the new personal chat; pass None to remove the chat. Use :meth:`~pyrogram.Client.get_created_chats` with ``is_suitable_for_my_personal_chat`` to get suitable chats

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Update your personal chat
                await app.set_personal_chat(chat_id="@Pyrogram")

                # Hide your personal chat
                await app.set_personal_chat()
        """

        return bool(
            await self.invoke(
                raw.functions.account.UpdatePersonalChannel(
                    channel=await self.resolve_peer(
                        chat_id
                    ) if chat_id else raw.types.InputChannelEmpty()
                )
            )
        )
