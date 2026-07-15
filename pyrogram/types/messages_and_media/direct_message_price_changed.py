#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram

from pyrogram import raw, types
from ..object import Object


class DirectMessagePriceChanged(Object):
    """Describes a service message about a change in the price of direct messages sent to a channel chat.

    Parameters:
        are_direct_messages_enabled (``bool``):
            True, if direct messages are enabled for the channel chat; False otherwise.

        direct_message_star_count (``int``, *optional*):
            The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        are_direct_messages_enabled: bool = None,
        direct_message_star_count: int = 0,
    ):
        super().__init__(client)

        self.are_direct_messages_enabled = are_direct_messages_enabled
        self.direct_message_star_count = direct_message_star_count


    @staticmethod
    def _parse_action(
        client,
        action: "raw.types.MessageActionPaidMessagesPrice"
    ) -> "DirectMessagePriceChanged":
        if isinstance(action, raw.types.MessageActionPaidMessagesPrice):
            return DirectMessagePriceChanged(
                client=client,
                are_direct_messages_enabled=True, #action.broadcast_messages_allowed,
                direct_message_star_count=action.stars,
            )
