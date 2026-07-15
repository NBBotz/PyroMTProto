#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .story_origin import StoryOrigin


class StoryOriginHiddenUser(StoryOrigin):
    """The original story was posted by an unknown user.

    Parameters:
        poster_name (``str``):
            Name of the user or the chat that posted the story.

    """

    def __init__(
        self,
        *,
        poster_name: str = None
    ):
        super().__init__()

        self.poster_name = poster_name
