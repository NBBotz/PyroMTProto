#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram

from pyrogram import raw, types
from ..object import Object



class GiveawayCompleted(Object):
    """This object represents a service message about the completion of a giveaway without public winners.

    Parameters:
        winner_count (``int``):
            Number of winners in the giveaway
        
        unclaimed_prize_count (``int``, *optional*):
            Number of undistributed prizes

        giveaway_message (:obj:`~pyrogram.types.Message`, *optional*):
            Message with the giveaway that was completed, if it wasn't deleted

        is_star_giveaway (``bool``, *optional*):
            True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        winner_count: int,
        unclaimed_prize_count: int = None,
        giveaway_message: "types.Message" = None,
        is_star_giveaway: bool = None
    ):
        super().__init__(client)

        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message
        self.is_star_giveaway = is_star_giveaway


    @staticmethod
    def _parse(
        client,
        giveaway_results: "raw.types.MessageActionGiveawayResults",
        message_id: int = None
    ) -> "GiveawayCompleted":
        if isinstance(giveaway_results, raw.types.MessageActionGiveawayResults):
            return GiveawayCompleted(
                client=client,
                winner_count=giveaway_results.winners_count,
                unclaimed_prize_count=getattr(giveaway_results, "unclaimed_count", None),
                giveaway_message=types.Message(
                    client=client,
                    id=message_id
                ) if message_id else None,
                is_star_giveaway=getattr(giveaway_results, "stars", None),
            )
