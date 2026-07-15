#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram

from pyrogram import raw, types
from ..object import Object



class GiveawayCreated(Object):
    """This object represents a service message about the creation of a scheduled giveaway.

    Parameters:
        prize_star_count (``int``, *optional*):
            The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        prize_star_count: int = None
    ):
        super().__init__(client)

        self.prize_star_count = prize_star_count


    @staticmethod
    def _parse(
        client,
        giveaway_launch: "raw.types.MessageActionGiveawayLaunch"
    ) -> "GiveawayCreated":
        if isinstance(giveaway_launch, raw.types.MessageActionGiveawayLaunch):
            return GiveawayCreated(
                client=client,
                prize_star_count=getattr(giveaway_launch, "stars", None)
            )
