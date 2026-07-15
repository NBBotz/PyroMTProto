#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw

from .story_area_type import StoryAreaType


class StoryAreaTypeUniqueGift(StoryAreaType):
    """This object describes a story area pointing to a unique gift. Currently, a story can have at most 1 unique gift area.

    Parameters:
        name (``str``):
            Unique name of the gift.

    """

    def __init__(
        self,
        name: str = None,
    ):
        super().__init__()

        self.name = name

    async def write(
        self,
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ):
        return raw.types.MediaAreaStarGift(
            coordinates=coordinates,
            slug=self.name
        )
