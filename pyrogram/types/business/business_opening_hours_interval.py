#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class BusinessOpeningHoursInterval(Object):
    """

    Parameters:
        opening_minute (``int``):
            The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60

        closing_minute (``int``):
            The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60

    """

    def __init__(
        self,
        *,
        opening_minute: int = None,
        closing_minute: int = None
    ):
        super().__init__()

        self.opening_minute = opening_minute
        self.closing_minute = closing_minute


    @staticmethod
    def _parse(
        weekly_open_: "raw.types.BusinessWeeklyOpen"
    ) -> "BusinessOpeningHoursInterval":
        return BusinessOpeningHoursInterval(
            opening_minute=weekly_open_.start_minute,
            closing_minute=weekly_open_.end_minute
        )
