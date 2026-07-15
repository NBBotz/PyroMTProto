#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    InputChannel = Union[raw.types.InputChannel, raw.types.InputChannelEmpty, raw.types.InputChannelFromMessage]
else:
    # noinspection PyRedeclaration
    class InputChannel(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputChannel
            InputChannelEmpty
            InputChannelFromMessage
        """

        QUALNAME = "pyrogram.raw.base.InputChannel"
        __union_types__ = Union[raw.types.InputChannel, raw.types.InputChannelEmpty, raw.types.InputChannelFromMessage]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/input-channel"
            )
