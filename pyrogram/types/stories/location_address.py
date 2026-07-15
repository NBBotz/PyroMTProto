#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class LocationAddress(Object):
    """This object describes the physical address of a location.

    Parameters:
        country_code (``str``):
            The two-letter ISO 3166-1 alpha-2 country code of the country where the location is located.

        state (``str``, *optional*):
            State of the location.

        city (``str``, *optional*):
            City of the location.
        
        street (``str``, *optional*):
            Street address of the location.

    """

    def __init__(
        self,
        country_code: str = None,
        state: str = None,
        city: str = None,
        street: str = None,
    ):
        super().__init__()

        self.country_code = country_code
        self.state = state
        self.city = city
        self.street = street
