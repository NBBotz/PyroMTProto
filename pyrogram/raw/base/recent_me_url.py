#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    RecentMeUrl = Union[raw.types.RecentMeUrlChat, raw.types.RecentMeUrlChatInvite, raw.types.RecentMeUrlStickerSet, raw.types.RecentMeUrlUnknown, raw.types.RecentMeUrlUser]
else:
    # noinspection PyRedeclaration
    class RecentMeUrl(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            RecentMeUrlChat
            RecentMeUrlChatInvite
            RecentMeUrlStickerSet
            RecentMeUrlUnknown
            RecentMeUrlUser
        """

        QUALNAME = "pyrogram.raw.base.RecentMeUrl"
        __union_types__ = Union[raw.types.RecentMeUrlChat, raw.types.RecentMeUrlChatInvite, raw.types.RecentMeUrlStickerSet, raw.types.RecentMeUrlUnknown, raw.types.RecentMeUrlUser]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/recent-me-url"
            )
