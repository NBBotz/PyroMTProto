#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw


class UpdateProfile:
    async def update_profile(
        self: "pyrogram.Client",
        *,
        first_name: str = None,
        last_name: str = None,
        bio: str = None
    ) -> bool:
        """Update your profile details such as first name, last name and bio.

        You can omit the parameters you don't want to change.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            first_name (``str``, *optional*):
                The new first name; 1-64 characters.

            last_name (``str``, *optional*):
                The new last name; 1-64 characters.
                Pass "" (empty string) to remove it.

            bio (``str``, *optional*):
                Changes the bio of the current user.
                Max ``intro_description_length_limit`` characters without line feeds.
                Pass "" (empty string) to remove it.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Update your first name only
                await app.update_profile(first_name="Pyrogram")

                # Update first name and bio
                await app.update_profile(first_name="Pyrogram", bio="https://github.com/TelegramPlayground/pyrogram")

                # Remove the last name
                await app.update_profile(last_name="")
        """

        return bool(
            await self.invoke(
                raw.functions.account.UpdateProfile(
                    first_name=first_name,
                    last_name=last_name,
                    about=bio
                )
            )
        )
