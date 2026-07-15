#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, utils


class ShowGift:
    async def show_gift(
        self: "pyrogram.Client",
        owned_gift_id: str
    ) -> bool:
        """Display gift on the current user's or the channel's profile page.

        .. note::

            Requires `can_post_messages` administrator right in the channel chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owned_gift_id (``str``):
                Unique identifier of the target gift.
                For a user gift, you can use the message ID (int) of the gift message.
                For a channel gift, you can use the packed format `chatID_savedID` (str).
                For a upgraded gift, you can use the gift link.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Show gift in user profile
                await app.show_gift(owned_gift_id="123")

                # Show gift in channel (owned_gift_id packed in format chatID_savedID)
                await app.show_gift(owned_gift_id="123_456")
        """
        r = await self.invoke(
            raw.functions.payments.SaveStarGift(
                stargift=await utils.get_input_stargift(self, owned_gift_id),
                unsave=False
            )
        )

        return r

