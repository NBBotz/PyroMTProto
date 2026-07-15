#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram

from pyrogram import raw, types
from ..object import Object


class PaidMessagesRefunded(Object):
    """Describes a service message about refunded paid messages.

    Parameters:
        message_count (``int``):
            The number of refunded messages.

        star_count (``int``):
            The number of refunded Telegram Stars.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        message_count: int = None,
        star_count: int = None
    ):
        super().__init__(client)

        self.message_count = message_count
        self.star_count = star_count


    @staticmethod
    def _parse_action(
        client,
        action: "raw.types.MessageActionPaidMessagesRefunded"
    ) -> "PaidMessagesRefunded":
        if isinstance(action, raw.types.MessageActionPaidMessagesRefunded):
            return PaidMessagesRefunded(
                client=client,
                message_count=action.count,
                star_count=action.stars
            )
