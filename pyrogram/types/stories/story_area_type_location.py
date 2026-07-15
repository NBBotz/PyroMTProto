#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import types, raw

from .story_area_type import StoryAreaType


class StoryAreaTypeLocation(StoryAreaType):
    """This object describes a story area pointing to a location. Currently, a story can have up to 10 location areas.

    Parameters:
        latitude (``float``):
            Location latitude in degrees.

        longitude (``float``):
            Location longitude in degrees.

        horizontal_accuracy (``float``, *optional*):
            The radius of uncertainty for the location, measured in meters; 0-1500.

        address (:obj:`~pyrogram.types.LocationAddress`, *optional*):
            Address of the location.

    """

    def __init__(
        self,
        latitude: float = None,
        longitude: float = None,
        horizontal_accuracy: float = 0,
        address: Optional["types.LocationAddress"] = None,
    ):
        super().__init__()

        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.address = address

    async def write(
        self,
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ):
        return raw.types.MediaAreaGeoPoint(
            coordinates=coordinates,
            geo=raw.types.GeoPoint(
                long=self.longitude,
                lat=self.latitude,
                access_hash=0,
                accuracy_radius=self.horizontal_accuracy
            ),
            address=raw.types.GeoPointAddress(
                country_iso2=self.address.country_code,
                state=self.address.state,
                city=self.address.city,
                street=self.address.street
            ) if self.address else None
        )
