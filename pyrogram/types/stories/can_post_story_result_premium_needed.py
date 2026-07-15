#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .can_post_story_result import CanPostStoryResult


class CanPostStoryResultPremiumNeeded(CanPostStoryResult):
    """The user must subscribe to Telegram Premium to be able to post stories.
    """

    def __init__(self,):
        super().__init__()
