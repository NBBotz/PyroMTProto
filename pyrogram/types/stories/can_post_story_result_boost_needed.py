#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .can_post_story_result import CanPostStoryResult


class CanPostStoryResultBoostNeeded(CanPostStoryResult):
    """The chat must be boosted first by Telegram Premium subscribers to post more stories.
    
    Call getChatBoostStatus to get current boost status of the chat.
    """

    def __init__(self,):
        super().__init__()
