#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class ShippingAddress(Object):
    """This object represents a shipping address.

    Parameters:
        country_code (``str``):
            Two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ country code.

        state (``str``):
            State, if applicable.

        city (``str``):
            City.

        street_line1 (``str``):
            First line for the address.

        street_line2 (``str``):
            Second line for the address.

        post_code (``str``):
            Address post code.

    """

    def __init__(
        self,
        *,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str
    ):
        super().__init__()

        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code
