#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class TransferGift:
    async def transfer_gift(
        self: "pyrogram.Client",
        gift_id: int,
        to_user_id: Union[int, str],
    ) -> bool:
        """Transfer a Unique Gift (upgraded NFT gift) to another user.

        Only Unique Gifts (upgraded star gifts) can be transferred.
        Regular star gifts cannot be transferred — convert or upgrade them first.

        Parameters:
            gift_id (``int``):
                ID of the unique gift to transfer.

            to_user_id (``int`` | ``str``):
                Target user's ID or username to receive the gift.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.transfer_gift(
                    gift_id=unique_gift_id,
                    to_user_id="friend_username"
                )
        """
        target_peer = await self.resolve_peer(to_user_id)
        await self.invoke(
            raw.functions.payments.TransferStarGift(
                stargift=raw.types.InputSavedStarGiftSlug(slug=str(gift_id)),
                to_id=target_peer,
            )
        )
        return True
