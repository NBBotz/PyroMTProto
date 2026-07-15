#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class UpgradeGift:
    async def upgrade_gift(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        message_id: int,
        keep_original_details: bool = True,
    ) -> bool:
        """Upgrade a regular star gift into a Unique Gift (NFT).

        Unique Gifts have rarity attributes and can be transferred/sold.
        Upgrading costs additional Stars (shown in the gift preview).

        Parameters:
            user_id (``int`` | ``str``):
                Your own user ID (or ``"me"``).

            message_id (``int``):
                ID of the service message containing the gift to upgrade.

            keep_original_details (``bool``, *optional*):
                If True (default), preserve the original sender's name and
                gift message in the upgraded gift's metadata.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.upgrade_gift("me", message_id=789)
        """
        peer = await self.resolve_peer(user_id)
        await self.invoke(
            raw.functions.payments.UpgradeStarGift(
                stargift=raw.types.InputSavedStarGiftUser(
                    user_id=peer,
                    msg_id=message_id,
                ),
                keep_original_details=keep_original_details,
            )
        )
        return True
