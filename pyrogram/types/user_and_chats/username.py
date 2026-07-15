#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw
from ..object import Object


class Username(Object):
    """Describes usernames assigned to a user, a supergroup, or a channel.

    Parameters:
        username (``str``):
            User's or chat's username.
        is_editable (``bool``, *optional*):
            True, if the username is editable.
        is_active (``bool``, *optional*):
            True, if the username is active.
    """

    def __init__(
        self, *,
        username: str,
        is_editable: bool = None,
        is_active: bool = None
    ):
        super().__init__()

        self.username = username
        self.is_editable = is_editable
        self.is_active = is_active

    @staticmethod
    def _parse(username: "raw.types.Username") -> "Username":
        return Username(
            username=username.username,
            is_editable=username.editable,
            is_active=username.active
        )
