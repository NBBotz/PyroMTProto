#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .can_post_story_result import CanPostStoryResult


class CanPostStoryResultOk(CanPostStoryResult):
    """A story can be sent.

    Parameters:
        story_count (``int``):
            Number of stories that can be posted by the user.

    """

    def __init__(
        self,
        story_count: int = None,
    ):
        super().__init__()

        self.story_count = story_count
