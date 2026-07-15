#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw

from .story_area_type import StoryAreaType


class StoryAreaTypeLink(StoryAreaType):
    """This object describes a story area pointing to an HTTP or tg:// link. Currently, a story can have up to 3 link areas.

    Parameters:
        url (``str``):
            HTTP or tg:// URL to be opened when the area is clicked.

    """

    def __init__(
        self,
        url: str = None,
    ):
        super().__init__()

        self.url = url

    async def write(
        self,
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ):
        return raw.types.MediaAreaUrl(
            coordinates=coordinates,
            url=self.url
        )
