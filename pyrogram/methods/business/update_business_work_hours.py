#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional
import pyrogram
from pyrogram import raw, types


class UpdateBusinessWorkHours:
    async def update_business_work_hours(
        self: "pyrogram.Client",
        timezone: Optional[str] = None,
        intervals: Optional[list] = None,
        open_now: bool = False,
    ) -> bool:
        """Set or update your Telegram Business working hours.

        Parameters:
            timezone (``str``, *optional*):
                IANA timezone name (e.g. ``"America/New_York"``).
                Required when setting hours. Pass None to clear all hours.

            intervals (``list`` of :obj:`~pyrogram.types.BusinessOpeningHoursInterval`, *optional*):
                List of weekly time intervals when you are open.
                Each interval has ``open_minute`` and ``close_minute``
                (minutes since Sunday 00:00 in the given timezone).

            open_now (``bool``, *optional*):
                If True, marks the business as currently open even outside
                the defined hours. Defaults to False.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                from pyrogram.types import BusinessOpeningHoursInterval

                # Mon–Fri 09:00–18:00 UTC
                intervals = [
                    BusinessOpeningHoursInterval(
                        open_minute=1440 + 9 * 60,    # Mon 09:00
                        close_minute=1440 + 18 * 60   # Mon 18:00
                    ),
                    # ... add more intervals for each day
                ]
                await app.update_business_work_hours(
                    timezone="UTC",
                    intervals=intervals
                )

                # Clear work hours
                await app.update_business_work_hours()
        """
        work_hours = None
        if timezone is not None and intervals is not None:
            raw_intervals = []
            for iv in intervals:
                if isinstance(iv, raw.types.BusinessWeeklyOpen):
                    raw_intervals.append(iv)
                else:
                    raw_intervals.append(
                        raw.types.BusinessWeeklyOpen(
                            start_minute=getattr(iv, "open_minute", iv[0]),
                            end_minute=getattr(iv, "close_minute", iv[1]),
                        )
                    )
            work_hours = raw.types.BusinessWorkHours(
                timezone_id=timezone,
                weekly_open=raw_intervals,
                open_now=open_now,
            )

        await self.invoke(
            raw.functions.account.UpdateBusinessWorkHours(business_work_hours=work_hours)
        )
        return True
