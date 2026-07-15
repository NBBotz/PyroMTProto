#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram
from pyrogram import types

from ..object import Object


class PollOption(Object):
    """Contains information about one answer option in a poll.

    Parameters:
        persistent_id (``str``):
            Unique identifier of the option, persistent on option addition and deletion.

        text (:obj:`~pyrogram.types.FormattedText`):
            Option text, 1-100 characters.

        voter_count (``int``):
            Number of users that voted for this option.
            Equals to 0 until you vote.

        added_by_user (:obj:`~pyrogram.types.User`, *optional*):
            User who added the option; omitted if the option wasn't added by a user after poll creation.
        
        added_by_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Chat that added the option; omitted if the option wasn't added by a chat after poll creation.
        
        addition_date (:py:obj:`~datetime.datetime`, *optional*):
            Date the message was last edited.

        data (``bytes``):
            The data this poll option is holding.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        persistent_id: str,
        text: "types.FormattedText",
        voter_count: int,
        data: bytes,
        added_by_user: "types.User" = None,
        added_by_chat: "types.Chat" = None,
        addition_date: datetime = None,
    ):
        super().__init__(client)

        self.persistent_id = persistent_id
        self.text = text
        self.voter_count = voter_count
        self.data = data
        self.added_by_user = added_by_user
        self.added_by_chat = added_by_chat
        self.addition_date = addition_date
