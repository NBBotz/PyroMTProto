#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw

from .story_area_type import StoryAreaType


class StoryAreaTypeMessage(StoryAreaType):
    """This object describes an area pointing to a message. Currently, a story can have up to 1 message area.

    Parameters:
        chat_id (``int`` | ``str``):
            Unique identifier (int) or username (str) of the target chat.
        
        message_id (``int``):
            Identifier of the message.

    """

    def __init__(
        self,
        chat_id: Union[int, str] = None,
        message_id: int = None,
    ):
        super().__init__()

        self.chat_id = chat_id
        self.message_id = message_id

    async def write(
        self,
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ):
        return raw.types.InputMediaAreaChannelPost(
            coordinates=coordinates,
            channel=await client.resolve_peer(self.chat_id),
            msg_id=self.message_id
        )
