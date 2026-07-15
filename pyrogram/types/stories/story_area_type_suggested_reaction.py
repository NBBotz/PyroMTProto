#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

import pyrogram
from pyrogram import types, raw

from .story_area_type import StoryAreaType


class StoryAreaTypeSuggestedReaction(StoryAreaType):
    """This object describes a story area pointing to a suggested reaction. Currently, a story can have up to 5 suggested reaction areas.

    Parameters:
        reaction_type (:obj:`~pyrogram.types.ReactionType`):
            Type of the reaction.

        is_dark (``bool``, *optional*):
            Pass True if the reaction area has a dark background.

        is_flipped (``bool``, *optional*):
            Pass True if reaction area corner is flipped.

    """

    def __init__(
        self,
        reaction_type: "types.ReactionType" = None,
        is_dark: Optional[bool] = None,
        is_flipped: Optional[bool] = None,
    ):
        super().__init__()

        self.reaction_type = reaction_type
        self.is_dark = is_dark
        self.is_flipped = is_flipped

    async def write(
        self,
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ):
        return raw.types.MediaAreaSuggestedReaction(
            dark=self.is_dark,
            flipped=self.is_flipped,
            coordinates=coordinates,
            reaction=self.reaction_type.write(client)
        )
