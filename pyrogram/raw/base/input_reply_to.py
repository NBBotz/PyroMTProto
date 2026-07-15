#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    InputReplyTo = Union[raw.types.InputReplyToMessage, raw.types.InputReplyToMonoForum, raw.types.InputReplyToStory]
else:
    # noinspection PyRedeclaration
    class InputReplyTo(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputReplyToMessage
            InputReplyToMonoForum
            InputReplyToStory
        """

        QUALNAME = "pyrogram.raw.base.InputReplyTo"
        __union_types__ = Union[raw.types.InputReplyToMessage, raw.types.InputReplyToMonoForum, raw.types.InputReplyToStory]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/input-reply-to"
            )
