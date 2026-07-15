#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram

from pyrogram import raw, types
from ..object import Object


class PaidMessagePriceChanged(Object):
    """Describes a service message about a change in the price of paid messages within a chat.

    Parameters:
        paid_message_star_count (``int``):
            The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        paid_message_star_count: int = None
    ):
        super().__init__(client)

        self.paid_message_star_count = paid_message_star_count


    @staticmethod
    def _parse_action(
        client,
        action: "raw.types.MessageActionPaidMessagesPrice"
    ) -> "PaidMessagePriceChanged":
        if isinstance(action, raw.types.MessageActionPaidMessagesPrice):
            return PaidMessagePriceChanged(
                client=client,
                paid_message_star_count=action.stars
            )
