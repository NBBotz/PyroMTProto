#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    WebPageAttribute = Union[raw.types.WebPageAttributeAiComposeTone, raw.types.WebPageAttributeStarGiftAuction, raw.types.WebPageAttributeStarGiftCollection, raw.types.WebPageAttributeStickerSet, raw.types.WebPageAttributeStory, raw.types.WebPageAttributeTheme, raw.types.WebPageAttributeUniqueStarGift]
else:
    # noinspection PyRedeclaration
    class WebPageAttribute(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebPageAttributeAiComposeTone
            WebPageAttributeStarGiftAuction
            WebPageAttributeStarGiftCollection
            WebPageAttributeStickerSet
            WebPageAttributeStory
            WebPageAttributeTheme
            WebPageAttributeUniqueStarGift
        """

        QUALNAME = "pyrogram.raw.base.WebPageAttribute"
        __union_types__ = Union[raw.types.WebPageAttributeAiComposeTone, raw.types.WebPageAttributeStarGiftAuction, raw.types.WebPageAttributeStarGiftCollection, raw.types.WebPageAttributeStickerSet, raw.types.WebPageAttributeStory, raw.types.WebPageAttributeTheme, raw.types.WebPageAttributeUniqueStarGift]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/web-page-attribute"
            )
