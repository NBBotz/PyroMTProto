#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .can_post_story_result import CanPostStoryResult


class CanPostStoryResultLiveStoryIsActive(CanPostStoryResult):
    """The user or the chat has an active live story. The live story must be deleted first.

    Parameters:
        story_id (``int``):
            Identifier of the active live story.

    """

    def __init__(
        self,
        story_id: int,
    ):
        super().__init__()

        self.story_id = story_id
