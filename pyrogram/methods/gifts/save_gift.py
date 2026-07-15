#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class SaveGift:
    async def save_gift(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        message_id: int,
        unsave: bool = False,
    ) -> bool:
        """Save or hide a received star gift on your profile.

        Parameters:
            user_id (``int`` | ``str``):
                Your own user ID (or ``"me"``).

            message_id (``int``):
                ID of the service message containing the gift.

            unsave (``bool``, *optional*):
                Pass True to hide the gift from your profile.
                Defaults to False (saves/shows the gift).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Show a gift on profile
                await app.save_gift("me", message_id=123)

                # Hide a gift from profile
                await app.save_gift("me", message_id=123, unsave=True)
        """
        peer = await self.resolve_peer(user_id)
        await self.invoke(
            raw.functions.payments.SaveStarGift(
                stargift=raw.types.InputSavedStarGiftUser(
                    user_id=peer,
                    msg_id=message_id,
                ),
                unsave=unsave,
            )
        )
        return True
