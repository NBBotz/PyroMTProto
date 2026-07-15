#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ChatHasProtectedContentToggled(Object):
    """Describes a service message about a chat ``has_protected_content`` setting was changed or request to change it was rejected.

    Parameters:
        request_message_id (``int``):
            Identifier of the message with the request to change the setting; can be an identifier of a deleted message or 0.

        old_has_protected_content (``bool``):
            Previous value of the setting.

        new_has_protected_content (``bool``):
            New value of the setting.

    """

    def __init__(
        self, *,
        request_message_id: int = None,
        old_has_protected_content: bool = None,
        new_has_protected_content: bool = None,
    ):
        super().__init__()

        self.request_message_id = request_message_id
        self.old_has_protected_content = old_has_protected_content
        self.new_has_protected_content = new_has_protected_content

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message: "raw.types.MessageService",
    ) -> "ChatHasProtectedContentToggled":
        action: "raw.types.MessageActionNoForwardsToggle" = message.action
        if isinstance(action, raw.types.MessageActionNoForwardsToggle):
            return ChatHasProtectedContentToggled(
                request_message_id=message.id,
                old_has_protected_content=action.prev_value,
                new_has_protected_content=action.new_value,
            )
