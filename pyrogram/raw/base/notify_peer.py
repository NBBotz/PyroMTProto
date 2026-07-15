#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    NotifyPeer = Union[raw.types.NotifyBroadcasts, raw.types.NotifyChats, raw.types.NotifyForumTopic, raw.types.NotifyPeer, raw.types.NotifyUsers]
else:
    # noinspection PyRedeclaration
    class NotifyPeer(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            NotifyBroadcasts
            NotifyChats
            NotifyForumTopic
            NotifyPeer
            NotifyUsers
        """

        QUALNAME = "pyrogram.raw.base.NotifyPeer"
        __union_types__ = Union[raw.types.NotifyBroadcasts, raw.types.NotifyChats, raw.types.NotifyForumTopic, raw.types.NotifyPeer, raw.types.NotifyUsers]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/notify-peer"
            )
