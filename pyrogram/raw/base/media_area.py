#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    MediaArea = Union[raw.types.InputMediaAreaChannelPost, raw.types.InputMediaAreaVenue, raw.types.MediaAreaChannelPost, raw.types.MediaAreaGeoPoint, raw.types.MediaAreaStarGift, raw.types.MediaAreaSuggestedReaction, raw.types.MediaAreaUrl, raw.types.MediaAreaVenue, raw.types.MediaAreaWeather]
else:
    # noinspection PyRedeclaration
    class MediaArea(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 9 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMediaAreaChannelPost
            InputMediaAreaVenue
            MediaAreaChannelPost
            MediaAreaGeoPoint
            MediaAreaStarGift
            MediaAreaSuggestedReaction
            MediaAreaUrl
            MediaAreaVenue
            MediaAreaWeather
        """

        QUALNAME = "pyrogram.raw.base.MediaArea"
        __union_types__ = Union[raw.types.InputMediaAreaChannelPost, raw.types.InputMediaAreaVenue, raw.types.MediaAreaChannelPost, raw.types.MediaAreaGeoPoint, raw.types.MediaAreaStarGift, raw.types.MediaAreaSuggestedReaction, raw.types.MediaAreaUrl, raw.types.MediaAreaVenue, raw.types.MediaAreaWeather]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/media-area"
            )
