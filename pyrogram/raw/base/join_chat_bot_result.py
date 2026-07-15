#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    JoinChatBotResult = Union[raw.types.JoinChatBotResultApproved, raw.types.JoinChatBotResultDeclined, raw.types.JoinChatBotResultQueued, raw.types.JoinChatBotResultWebView]
else:
    # noinspection PyRedeclaration
    class JoinChatBotResult(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            JoinChatBotResultApproved
            JoinChatBotResultDeclined
            JoinChatBotResultQueued
            JoinChatBotResultWebView
        """

        QUALNAME = "pyrogram.raw.base.JoinChatBotResult"
        __union_types__ = Union[raw.types.JoinChatBotResultApproved, raw.types.JoinChatBotResultDeclined, raw.types.JoinChatBotResultQueued, raw.types.JoinChatBotResultWebView]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/join-chat-bot-result"
            )
