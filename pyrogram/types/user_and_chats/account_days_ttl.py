#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class AccountDaysTTL(Object):
    """Account auto-delete TTL setting.

    Parameters:
        days (``int``):
            Number of days after which the account is deleted if inactive.
            Valid values: 30, 90, 180, 365.
    """

    def __init__(self, *, days: int):
        super().__init__()
        self.days = days

    @staticmethod
    def _parse(ttl) -> "AccountDaysTTL":
        return AccountDaysTTL(days=ttl.days)

    def write(self):
        from pyrogram import raw
        return raw.types.AccountDaysTTL(days=self.days)
