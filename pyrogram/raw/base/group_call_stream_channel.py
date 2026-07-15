#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    GroupCallStreamChannel = Union[raw.types.GroupCallStreamChannel]
else:
    # noinspection PyRedeclaration
    class GroupCallStreamChannel(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            GroupCallStreamChannel
        """

        QUALNAME = "pyrogram.raw.base.GroupCallStreamChannel"
        __union_types__ = Union[raw.types.GroupCallStreamChannel]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/group-call-stream-channel"
            )
