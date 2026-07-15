#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class GetGiftUpgradePreview:
    async def get_gift_upgrade_preview(
        self: "pyrogram.Client",
        gift_id: int,
    ):
        """Get a preview of the possible upgrade attributes for a star gift.

        Shows what model, backdrop, and symbol the gift could get when upgraded.
        Useful for showing users what their gift might become.

        Parameters:
            gift_id (``int``):
                The star gift type ID to preview upgrade attributes for.

        Returns:
            :obj:`~pyrogram.raw.types.payments.StarGiftUpgradePreview` with
            ``models``, ``backdrops``, and ``symbols`` attribute lists.

        Example:
            .. code-block:: python

                preview = await app.get_gift_upgrade_preview(gift_id=123)
                print(f"Possible models: {len(preview.models)}")
        """
        return await self.invoke(
            raw.functions.payments.GetStarGiftUpgradePreview(
                gift_id=gift_id
            )
        )
