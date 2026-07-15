#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types
from ..object import Object


class PaidMediaInfo(Object):
    """Describes the paid media added to a message.

    Parameters:
        star_count (``int``):
            The number of Telegram Stars that must be paid to buy access to the media.

        paid_media  (List of :obj:`~pyrogram.types.PaidMedia`):
            Information about the paid media.

    """

    def __init__(
        self,
        *,
        star_count: str,
        paid_media: list["types.PaidMedia"]
    ):
        super().__init__()

        self.star_count = star_count
        self.paid_media = paid_media


    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message_paid_media: "raw.types.MessageMediaPaidMedia"
    ) -> "PaidMediaInfo":
        return PaidMediaInfo(
            star_count=message_paid_media.stars_amount,
            paid_media=[
                types.PaidMedia._parse(client, em)
                for em in message_paid_media.extended_media
            ]
        )
