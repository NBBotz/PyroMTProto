#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw, types


class SuggestBirthday:
    async def suggest_birthday(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        birthday: "types.Birthday"
    ) -> bool:
        """Suggests a birthdate to another regular user with common messages and allowing non-paid messages.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            birthday (:obj:`types.Birthday`):
                Birthdate to suggest.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.suggest_birthday(chat_id=123456, birthday=types.Birthday(day=1, month=1, year=2000))
        """
        await self.invoke(
            raw.functions.users.SuggestBirthday(
                id=await self.resolve_peer(chat_id),
                birthday=birthday.write()
            )
        )

        return True

