#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class ConvertGift:
    async def convert_gift(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        message_id: int,
    ) -> bool:
        """Convert a received star gift into Telegram Stars.

        Once converted, the gift is removed and its Stars value is
        added to your balance. This action is irreversible.

        Parameters:
            user_id (``int`` | ``str``):
                Your own user ID (or ``"me"``).

            message_id (``int``):
                ID of the service message containing the gift.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.convert_gift("me", message_id=456)
        """
        peer = await self.resolve_peer(user_id)
        await self.invoke(
            raw.functions.payments.ConvertStarGift(
                stargift=raw.types.InputSavedStarGiftUser(
                    user_id=peer,
                    msg_id=message_id,
                ),
            )
        )
        return True
