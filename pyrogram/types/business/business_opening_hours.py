#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class BusinessOpeningHours(Object):
    """

    Parameters:
        time_zone_name (``str``):
            Unique name of the time zone for which the opening hours are defined

        opening_hours (List of :obj:`~pyrogram.types.BusinessOpeningHoursInterval`):
            List of time intervals describing business opening hours

    """

    def __init__(
        self,
        *,
        time_zone_name: str = None,
        opening_hours: list["types.BusinessOpeningHoursInterval"] = None,
        _raw: "raw.types.BusinessWorkHours" = None
    ):
        super().__init__()

        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours
        self._raw = _raw


    @staticmethod
    def _parse(
        client,
        business_work_hours: "raw.types.BusinessWorkHours"
    ) -> "BusinessOpeningHours":
        return BusinessOpeningHours(
            time_zone_name=getattr(business_work_hours, "timezone_id", None),
            opening_hours=types.List(
                [
                    types.BusinessOpeningHoursInterval._parse(
                        weekly_open_
                    ) for weekly_open_ in business_work_hours.weekly_open
                ]
            ) if getattr(business_work_hours, "weekly_open", None) else None,
            _raw=business_work_hours
        )
