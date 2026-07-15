#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import raw, types, utils, enums
from ..object import Object


class ForumTopicCreated(Object):
    """This object represents a service message about a new forum topic created in the chat.

    Parameters:
        name (``str``):
            Name of the topic

        icon_color  (``int``):
            Color of the topic icon in RGB format

        icon_custom_emoji_id (``str``, *optional*):
            Unique identifier of the custom emoji shown as the topic icon

        is_name_implicit (``bool``, *optional*):
            True, if the name of the topic wasn't specified explicitly by its creator and likely needs to be changed by the bot.

    """

    def __init__(
        self,
        *,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: str = None,
        is_name_implicit: bool = None,
    ):
        super().__init__()

        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id
        self.is_name_implicit = is_name_implicit


    @staticmethod
    def _parse(
        topic_create_action: "raw.types.MessageActionTopicCreate"
    ) -> "ForumTopicCreated":
        return ForumTopicCreated(
            name=topic_create_action.title,
            icon_color=topic_create_action.icon_color,  # TODO
            icon_custom_emoji_id=getattr(topic_create_action, "", None),
            is_name_implicit=getattr(topic_create_action, "title_missing", False),
        )
