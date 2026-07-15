#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import raw, types, utils, enums
from ..object import Object


class ForumTopicEdited(Object):
    """This object represents a service message about an edited forum topic.

    Parameters:
        name (``str``, *optional*):
            New name of the topic, if it was edited

        icon_custom_emoji_id (``str``, *optional*):
            New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed

    """

    def __init__(
        self,
        *,
        name: str = None,
        icon_custom_emoji_id: str = None
    ):
        super().__init__()

        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id


    @staticmethod
    def _parse(
        topic_edit_action: "raw.types.MessageActionTopicEdit"
    ) -> "ForumTopicEdited":
        return ForumTopicEdited(
            name=getattr(topic_edit_action, "title", None),
            icon_custom_emoji_id=getattr(topic_edit_action, "icon_emoji_id", None)
        )
