#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    EmojiStatuses = Union[raw.types.account.EmojiStatuses, raw.types.account.EmojiStatusesNotModified]
else:
    # noinspection PyRedeclaration
    class EmojiStatuses(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.EmojiStatuses
            account.EmojiStatusesNotModified

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetDefaultEmojiStatuses
            account.GetRecentEmojiStatuses
            account.GetChannelDefaultEmojiStatuses
            account.GetCollectibleEmojiStatuses
        """

        QUALNAME = "pyrogram.raw.base.account.EmojiStatuses"
        __union_types__ = Union[raw.types.account.EmojiStatuses, raw.types.account.EmojiStatusesNotModified]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/emoji-statuses"
            )
