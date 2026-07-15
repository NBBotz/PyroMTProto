#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .can_post_story_result import CanPostStoryResult


class CanPostStoryResultActiveStoryLimitExceeded(CanPostStoryResult):
    """The limit for the number of active stories exceeded. The user can buy Telegram Premium, delete an active story, or wait for the oldest story to expire.
    """

    def __init__(self,):
        super().__init__()
