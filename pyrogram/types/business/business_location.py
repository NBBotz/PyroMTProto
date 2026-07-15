#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class BusinessLocation(Object):
    """

    Parameters:
        address (``str``):
            Address of the business

        location (:obj:`~pyrogram.types.Location`, *optional*):
            Location of the business

    """

    def __init__(
        self,
        *,
        address: str = None,
        location: "types.Location" = None
    ):
        super().__init__()

        self.address = address
        self.location = location


    @staticmethod
    def _parse(
        client,
        business_location: "raw.types.BusinessLocation"
    ) -> "BusinessLocation":
        return BusinessLocation(
            address=getattr(business_location, "address", None),
            location=types.Location._parse(
                client,
                business_location.geo_point
            ) if getattr(business_location, "geo_point", None) else None
        )
