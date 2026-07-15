#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    BotInlineResult = Union[raw.types.BotInlineMediaResult, raw.types.BotInlineResult]
else:
    # noinspection PyRedeclaration
    class BotInlineResult(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotInlineMediaResult
            BotInlineResult
        """

        QUALNAME = "pyrogram.raw.base.BotInlineResult"
        __union_types__ = Union[raw.types.BotInlineMediaResult, raw.types.BotInlineResult]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/bot-inline-result"
            )
