#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ChatHasProtectedContentDisableRequested(Object):
    """Describes a service message about a chat ``has_protected_content`` setting was requested to be disabled.

    Parameters:
        is_expired (``bool``):
            True, if the request has expired.

        old_has_protected_content (``bool``):
            Previous value of the setting.

        new_has_protected_content (``bool``):
            New value of the setting.

    """

    def __init__(
        self, *,
        is_expired: bool = None,
        old_has_protected_content: bool = None,
        new_has_protected_content: bool = None,
    ):
        super().__init__()

        self.is_expired = is_expired
        self.old_has_protected_content = old_has_protected_content
        self.new_has_protected_content = new_has_protected_content

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        action: "raw.types.MessageActionNoForwardsRequest",
    ) -> "ChatHasProtectedContentDisableRequested":
        if isinstance(action, raw.types.MessageActionNoForwardsRequest):
            return ChatHasProtectedContentDisableRequested(
                is_expired=action.expired,
                old_has_protected_content=action.prev_value,
                new_has_protected_content=action.new_value,
            )
