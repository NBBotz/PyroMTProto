#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw
from ..object import Object


class ChatBoostAdded(Object):
    """This object represents a service message about a user boosting a chat.

    Parameters:
        boost_count (``int``):
            Number of boosts added by the user

    """

    def __init__(
        self,
        *,
        boost_count: int,
    ):
        super().__init__()

        self.boost_count = boost_count

    @staticmethod
    def _parse(action: "raw.types.MessageActionBoostApply"):
        return ChatBoostAdded(
            boost_count=action.boosts
        )
