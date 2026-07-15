#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ChatOwnerChanged(Object):
    """Describes a service message about an ownership change in the chat.

    Parameters:
        new_owner (:obj:`~pyrogram.types.User`):
            The new owner of the chat.

    """

    def __init__(self, *, new_owner: "types.User"):
        super().__init__()

        self.new_owner = new_owner

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        action: "raw.types.MessageActionChangeCreator",
        users: dict[int, "types.User"],
    ) -> "ChatOwnerChanged":
        if isinstance(action, raw.types.MessageActionChangeCreator):
            return ChatOwnerChanged(
                new_owner=types.User._parse(client, users.get(action.new_creator_id))
            )
