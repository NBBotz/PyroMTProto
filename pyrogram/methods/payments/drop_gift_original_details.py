#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional
import pyrogram
from pyrogram import raw, utils


class DropGiftOriginalDetails:
    async def drop_gift_original_details(
        self: "pyrogram.Client",
        owned_gift_id: str,
        star_count: Optional[int] = None,
    ) -> bool:
        """Drops original details for an upgraded gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owned_gift_id (``str``):
                Identifier of the gift.
                For a upgraded gift, you can use the gift link.

            star_count (``int``, *optional*):
                The amount of Telegram Stars required to pay for the upgrade.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Drop gift details
                await app.drop_gift_original_details(owned_gift_id="https://t.me/nft/EasterEgg-147453")
        """
        invoice = raw.types.InputInvoiceStarGiftDropOriginalDetails(
            stargift=await utils.get_input_stargift(self, owned_gift_id)
        )

        form = await self.invoke(
            raw.functions.payments.GetPaymentForm(
                invoice=invoice
            )
        )

        if star_count is not None:
            if star_count < 0:
                raise ValueError("Invalid amount of Telegram Stars specified.")

            if form.invoice.prices[0].amount > star_count:
                raise ValueError("Have not enough Telegram Stars.")

        await self.invoke(
            raw.functions.payments.SendStarsForm(
                form_id=form.form_id,
                invoice=invoice
            )
        )

        return True

