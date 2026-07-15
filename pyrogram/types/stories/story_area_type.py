#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class StoryAreaType(Object):
    """This object describes the type of a clickable area on a story.

    Currently, it can be one of:

    .. include:: /_includes/usable-by/users-bots.rst

    - :obj:`~pyrogram.types.StoryAreaTypeLocation`
    - :obj:`~pyrogram.types.StoryAreaTypeSuggestedReaction`
    - :obj:`~pyrogram.types.StoryAreaTypeLink`
    - :obj:`~pyrogram.types.StoryAreaTypeWeather`
    - :obj:`~pyrogram.types.StoryAreaTypeUniqueGift`

    .. include:: /_includes/usable-by/users.rst

    - :obj:`~pyrogram.types.StoryAreaTypeMessage`
    - :obj:`~pyrogram.types.StoryAreaTypeFoundVenue`

    """

    def __init__(self):
        super().__init__()
