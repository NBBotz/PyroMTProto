#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw

from ..object import Object


class Location(Object):
    """A point on the map.

    Parameters:
        longitude (``float``):
            Longitude as defined by sender.

        latitude (``float``):
            Latitude as defined by sender.

        accuracy_radius (``int``, *optional*):
            The estimated horizontal accuracy of the location, in meters as defined by the sender.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        longitude: float,
        latitude: float,
        accuracy_radius: Optional[int] = None,
    ):
        super().__init__(client)

        self.longitude = longitude
        self.latitude = latitude
        self.accuracy_radius = accuracy_radius

    @staticmethod
    def _parse(client, geo_point: "raw.base.GeoPoint") -> "Location":
        if isinstance(geo_point, raw.types.GeoPoint):
            return Location(
                longitude=geo_point.long,
                latitude=geo_point.lat,
                accuracy_radius=geo_point.accuracy_radius,
                client=client
            )

    async def write(self) -> "raw.types.InputMediaGeoPoint":
        return raw.types.InputMediaGeoPoint(
            geo_point=raw.types.InputGeoPoint(
                lat=self.latitude,
                long=self.longitude,
                accuracy_radius=self.accuracy_radius,
            ),
        )


class ChatLocation(Object):
    """Represents a location to which a chat is connected.
    
    Parameters:
        location (:obj:`~pyrogram.types.Location`):
            The location to which the supergroup is connected. Can't be a live location.
        
        address (``string``):
            Location address; 1-64 characters, as defined by the chat owner.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        location: "Location",
        address: str
    ):
        super().__init__(client)

        self.location = location
        self.address = address
