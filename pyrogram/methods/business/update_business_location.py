#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional
import pyrogram
from pyrogram import raw


class UpdateBusinessLocation:
    async def update_business_location(
        self: "pyrogram.Client",
        address: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
    ) -> bool:
        """Update the physical location shown on your Business profile.

        Parameters:
            address (``str``, *optional*):
                Text description of the location (e.g. street address).
                Pass None to clear the location entirely.

            latitude (``float``, *optional*):
                Geographical latitude of the location.
                Required when setting a map pin.

            longitude (``float``, *optional*):
                Geographical longitude of the location.
                Required when setting a map pin.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Set address with map pin
                await app.update_business_location(
                    address="123 Main St, Springfield",
                    latitude=37.7749,
                    longitude=-122.4194
                )

                # Set address only (no map pin)
                await app.update_business_location(address="123 Main St")

                # Clear location
                await app.update_business_location()
        """
        location = None
        if address is not None:
            geo_point = None
            if latitude is not None and longitude is not None:
                geo_point = raw.types.InputGeoPoint(
                    lat=latitude,
                    long=longitude,
                )
            location = raw.types.BusinessLocation(
                address=address,
                geo_point=geo_point,
            )

        await self.invoke(
            raw.functions.account.UpdateBusinessLocation(location=location)
        )
        return True
