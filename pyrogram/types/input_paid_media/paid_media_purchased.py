#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw, types

from ..object import Object


class PaidMediaPurchased(Object):
    """This object contains information about a paid media purchase.

    Parameters:
        from_user (:obj:`~pyrogram.types.User`):
            User who purchased the media.

        paid_media_payload (``str``):
            Bot-specified paid media payload.

    """

    def __init__(
        self,
        from_user: "types.User" = None,
        paid_media_payload: str = None,
        _raw: "raw.types.UpdateBotPurchasedPaidMedia" = None,
    ):
        super().__init__()

        self.from_user = from_user
        self.paid_media_payload = paid_media_payload
        self._raw = _raw


    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        bot_purchased_paid_media: "raw.types.UpdateBotPurchasedPaidMedia",
        users: dict,
    ) -> "PaidMediaPurchased":
        return PaidMediaPurchased(
            from_user=types.User._parse(client, users[bot_purchased_paid_media.user_id]),
            paid_media_payload=bot_purchased_paid_media.payload,
            _raw=bot_purchased_paid_media
        )
