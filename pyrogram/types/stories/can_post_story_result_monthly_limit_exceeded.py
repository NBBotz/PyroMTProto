#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .can_post_story_result import CanPostStoryResult


class CanPostStoryResultMonthlyLimitExceeded(CanPostStoryResult):
    """The monthly limit for the number of posted stories exceeded. The user needs to buy Telegram Premium or wait specified time.

    Parameters:
        retry_after (``int``):
            Time left before the user can post the next story.

    """

    def __init__(
        self,
        retry_after: int,
    ):
        super().__init__()

        self.retry_after = retry_after
