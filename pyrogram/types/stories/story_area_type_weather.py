#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw

from .story_area_type import StoryAreaType


class StoryAreaTypeWeather(StoryAreaType):
    """This object describes a story area containing weather information. Currently, a story can have up to 3 weather areas.

    Parameters:
        temperature (``float``):
            Temperature, in degree Celsius.

        emoji (``str``):
            Emoji representing the weather.

        background_color (``int``):
            A color of the area background in the ARGB format.

    """

    def __init__(
        self,
        temperature: float = None,
        emoji: str = None,
        background_color: int = None,
    ):
        super().__init__()

        self.temperature = temperature
        self.emoji = emoji
        self.background_color = background_color

    async def write(
        self,
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ):
        return raw.types.MediaAreaWeather(
            coordinates=coordinates,
            emoji=self.emoji,
            temperature_c=self.temperature,
            color=self.background_color
        )
