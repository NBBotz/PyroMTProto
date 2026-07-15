#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import types

from .story_origin import StoryOrigin


class StoryOriginPublicStory(StoryOrigin):
    """The original story was a public story that was posted by a known chat.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            Identifier of the chat that posted original story.
        
        story_id (``int``):
            Story identifier of the original story.

    """

    def __init__(
        self,
        *,
        chat: "types.Chat" = None,
        story_id: int = None
    ):
        super().__init__()

        self.chat = chat
        self.story_id = story_id
