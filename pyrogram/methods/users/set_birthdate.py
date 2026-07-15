#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import raw, types


class SetBirthdate:
    async def set_birthdate(
        self: "pyrogram.Client",
        birthdate: Optional["types.Birthdate"] = None
    ) -> bool:
        """Changes the birthdate of the current user 

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            birthdate (:obj:`~pyrogram.types.Birthdate`, *optional*):
                The new value of the current user's birthdate; pass None to remove the birthdate

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Update your birthdate
                await app.set_birthdate(birthdate=types.Birthdate(
                    day=15,
                    month=12,
                    year=2017
                ))

                # Remove your birthdate
                await app.set_birthdate()

        """

        return bool(
            await self.invoke(
                raw.functions.account.UpdateBirthday(
                    birthday=birthdate.write() if birthdate else None
                )
            )
        )
