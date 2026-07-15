#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw, types
from ..object import Object


class VideoChatParticipantsInvited(Object):
    """A service message about new members invited to a voice chat.


    Parameters:
        users (List of :obj:`~pyrogram.types.User`):
            New members that were invited to the voice chat.
    """

    def __init__(
        self, *,
        users: list["types.User"]
    ):
        super().__init__()

        self.users = users

    @staticmethod
    def _parse(
        client,
        action: "raw.types.MessageActionInviteToGroupCall",
        users: dict[int, "raw.types.User"]
    ) -> "VideoChatParticipantsInvited":
        users = [types.User._parse(client, users[i]) for i in action.users]

        return VideoChatParticipantsInvited(users=users)
