#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw

from ..object import Object


class StarAmount(Object):
    """This object Describes a possibly non-integer amount of Telegram Stars.

    Parameters:
        star_count (``int``):
            The integer amount of Telegram Stars rounded to 0.

        nanostar_count (``int``):
            The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999.

    """

    def __init__(
        self,
        *,
        star_count: int = None,
        nanostar_count: int = None,
    ):
        super().__init__()

        self.star_count = star_count
        self.nanostar_count = nanostar_count


    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        stars_status: "raw.base.payments.StarsStatus"
    ) -> "StarAmount":
        return StarAmount(
            star_count=stars_status.balance.amount,
            nanostar_count=stars_status.balance.nanos,
        )
