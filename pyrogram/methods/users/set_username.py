#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import raw


class SetUsername:
    async def set_username(
        self: "pyrogram.Client",
        username: Optional[str]
    ) -> bool:
        """Changes the editable username of the current user.

        This method only works for users, not bots.
        Bot usernames must be changed via Bot Support or by recreating them from scratch using BotFather.
        To set a channel or supergroup username you can use :meth:`~pyrogram.Client.set_chat_username`.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            username (``str`` | ``None``):
                Username to set. "" (empty string) or None to remove it.
                The username can't be completely removed if there is another active or disabled username.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_username("new_username")
        """

        return bool(
            await self.invoke(
                raw.functions.account.UpdateUsername(
                    username=username or ""
                )
            )
        )
