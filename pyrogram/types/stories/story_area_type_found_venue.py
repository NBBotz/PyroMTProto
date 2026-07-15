#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import types, raw

from .story_area_type import StoryAreaType


class StoryAreaTypeFoundVenue(StoryAreaType):
    """This object describes an area pointing to a venue found by the FOURSQUARE bot. Currently, a story can have up to 10 venue areas.

    Parameters:
        query_id (``int``):
            Identifier of the inline query, used to find the venue.

        result_id (``str``):
            Identifier of the inline query result.

    """

    def __init__(
        self,
        query_id: int = None,
        result_id: str = None,
    ):
        super().__init__()

        self.query_id = query_id
        self.result_id = result_id

    async def write(
        self,
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ):
        return raw.types.InputMediaAreaVenue(
            coordinates=coordinates,
            query_id=self.query_id,
            result_id=self.result_id,
        )
