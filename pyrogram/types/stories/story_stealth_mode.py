#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, utils

from ..object import Object


class StoryStealthMode(Object):
    """Story stealth mode.

    Parameters:
        active_until_date (``int``):
            Point in time (Unix timestamp) until stealth mode is active; None if it is disabled.

        cooldown_until_date (``int``):
            Point in time (Unix timestamp) when stealth mode can be enabled again; None if there is no active cooldown.

    """

    def __init__(
        self,
        *,
        active_until_date: int = None,
        cooldown_until_date: int = None,
    ):
        super().__init__()

        self.active_until_date = active_until_date
        self.cooldown_until_date = cooldown_until_date

    @staticmethod
    def _parse(ssm: "raw.types.StoriesStealthMode") -> "StoryStealthMode":
        return StoryStealthMode(
            active_until_date=utils.timestamp_to_datetime(getattr(ssm, "active_until_date", 0)),
            cooldown_until_date=utils.timestamp_to_datetime(getattr(ssm, "cooldown_until_date", 0)),
        )
