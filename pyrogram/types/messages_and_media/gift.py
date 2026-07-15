#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime
from typing import Optional, Union

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class Gift(Object):
    """Describes a gift that can be sent to another user.

    Parameters:
        id (``int``):
            Unique identifier of the gift.

        sticker (:obj:`~pyrogram.types.Sticker`):
            The sticker representing the gift.

        star_count (``int``):
            Number of Telegram Stars that must be paid for the gift.

        total_count (``int``, *optional*):
            Number of total times the gift can be purchased by all users; None if not limited.

        remaining_count (``int``, *optional*):
            Number of remaining times the gift can be purchased by all users; None if not limited or the gift was sold out.

        default_sell_star_count (``int``):
            Number of Telegram Stars that can be claimed by the receiver instead of the gift by default. If the gift was paid with just bought Telegram Stars, then full value can be claimed.

        upgrade_star_count (``int``, *optional*):
            Number of Telegram Stars that must be paid to upgrade the gift; 0 if upgrade isn't possible.

        is_for_birthday (``bool``, *optional*):
            True, if the gift is a birthday gift.

        first_send_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time (Unix timestamp) when the gift was send for the first time; for sold out gifts only.

        last_send_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time (Unix timestamp) when the gift was send for the last time; for sold out gifts only.

        is_limited (``bool``, *optional*):
            True, if the number of gifts is limited.

        is_sold_out (``bool``, *optional*):
            True, if the star gift is sold out.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        sticker: "types.Sticker",
        star_count: int,
        total_count: Optional[int] = None,
        remaining_count: Optional[int] = None,
        default_sell_star_count: int,
        upgrade_star_count: int,
        is_for_birthday: Optional[bool] = None,
        first_send_date: Optional[datetime] = None,
        last_send_date: Optional[datetime] = None,
        is_limited: Optional[bool] = None,
        is_sold_out: Optional[bool] = None,
    ):
        super().__init__(client)

        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.total_count = total_count
        self.remaining_count = remaining_count
        self.default_sell_star_count = default_sell_star_count
        self.upgrade_star_count = upgrade_star_count
        self.is_for_birthday = is_for_birthday
        self.first_send_date = first_send_date
        self.last_send_date = last_send_date
        self.is_limited = is_limited
        self.is_sold_out = is_sold_out

    @staticmethod
    async def _parse(
        client,
        star_gift: "raw.base.StarGift",
        users: dict
    ) -> Union["Gift", "types.UpgradedGift"]:
        if isinstance(star_gift, raw.types.StarGiftUnique):
            return types.UpgradedGift._parse(client, star_gift, users)

        doc = star_gift.sticker
        attributes = {type(i): i for i in doc.attributes}

        return Gift(
            id=star_gift.id,
            sticker=await types.Sticker._parse(client, doc, attributes),
            star_count=star_gift.stars,
            default_sell_star_count=star_gift.convert_stars,
            remaining_count=getattr(star_gift, "availability_remains", None),
            total_count=getattr(star_gift, "availability_total", None),
            first_send_date=utils.timestamp_to_datetime(getattr(star_gift, "first_sale_date", None)),
            last_send_date=utils.timestamp_to_datetime(getattr(star_gift, "last_sale_date", None)),
            is_limited=getattr(star_gift, "limited", None),
            is_sold_out=getattr(star_gift, "sold_out", None),
            upgrade_star_count=getattr(star_gift, "upgrade_stars", 0),
            is_for_birthday=getattr(star_gift, "birthday", None),
            client=client
        )
