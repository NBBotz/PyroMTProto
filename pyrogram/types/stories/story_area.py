#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import types, raw, utils

from ..object import Object


class StoryArea(Object):
    """This object describes a clickable area on a story media.

    Parameters:
        position (:obj:`~pyrogram.types.StoryAreaPosition`):
            Position of the area.
        
        type (:obj:`~pyrogram.types.StoryAreaType`):
            Type of the area.

    """

    def __init__(
        self,
        position: "types.StoryAreaPosition" = None,
        type: "types.StoryAreaType" = None,
    ):
        super().__init__()

        self.position = position
        self.type = type

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        area: "raw.base.MediaArea",
    ) -> "StoryArea":
        story_area_type = None
        if isinstance(area, raw.types.MediaAreaVenue):
            # coordinates:MediaAreaCoordinates geo:GeoPoint title:string address:string provider:string venue_id:string venue_type:string
            story_area_type = area
        if isinstance(area, raw.types.MediaAreaGeoPoint):
            story_area_type = types.StoryAreaTypeLocation(
                latitude=area.geo.lat,
                longitude=area.geo.long,
                horizontal_accuracy=area.geo.accuracy_radius,
                address=types.LocationAddress(
                    country_code=area.address.country_iso2,
                    state=area.address.state,
                    city=area.address.city,
                    street=area.address.street,
                ) if area.address else None
            )
        if isinstance(area, raw.types.MediaAreaSuggestedReaction):
            story_area_type = types.StoryAreaTypeSuggestedReaction(
                reaction_type=types.ReactionType._parse(client, area.reaction),
                is_dark=area.dark,
                is_flipped=area.flipped
            )
        if isinstance(area, raw.types.MediaAreaChannelPost):
            story_area_type = types.StoryAreaTypeMessage(
                chat_id=utils.get_channel_id(area.channel_id),
                message_id=area.msg_id
            )
        if isinstance(area, raw.types.MediaAreaUrl):
            story_area_type = types.StoryAreaTypeLink(
                url=area.url
            )
        if isinstance(area, raw.types.MediaAreaWeather):
            story_area_type = types.StoryAreaTypeWeather(
                temperature=area.temperature_c,
                emoji=area.emoji,
                background_color=area.color
            )
        if isinstance(area, raw.types.MediaAreaStarGift):
            story_area_type = types.StoryAreaTypeUniqueGift(
                name=area.slug
            )
        return StoryArea(
            position=types.StoryAreaPosition._parse(area.coordinates),
            type=story_area_type,
        )

    def write(self, client: "pyrogram.Client"):
        coordinates = self.position.write()
        return self.type.write(client, coordinates)
