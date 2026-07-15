#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import types, raw
from ..object import Object


class Birthdate(Object):
    """

    Parameters:
        day (``int``):
            Day of the user's birth; 1-31

        month (``int``):
            Month of the user's birth; 1-12

        year (``int``, *optional*):
            Year of the user's birth

    """

    def __init__(
        self,
        *,
        day: int,
        month: int,
        year: int = None
    ):
        super().__init__()

        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def _parse(
        birthday: "raw.types.Birthday"
    ) -> "Birthdate":
        return Birthdate(
            day=birthday.day,
            month=birthday.month,
            year=getattr(birthday, "year", None)
        )

    def write(self):
        return raw.types.Birthday(
            day=self.day,
            month=self.month,
            year=self.year
        )
