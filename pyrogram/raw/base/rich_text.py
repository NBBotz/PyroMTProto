#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    RichText = Union[raw.types.TextAnchor, raw.types.TextAutoEmail, raw.types.TextAutoPhone, raw.types.TextAutoUrl, raw.types.TextBankCard, raw.types.TextBold, raw.types.TextBotCommand, raw.types.TextCashtag, raw.types.TextConcat, raw.types.TextCustomEmoji, raw.types.TextDate, raw.types.TextEmail, raw.types.TextEmpty, raw.types.TextFixed, raw.types.TextHashtag, raw.types.TextImage, raw.types.TextItalic, raw.types.TextMarked, raw.types.TextMath, raw.types.TextMention, raw.types.TextMentionName, raw.types.TextPhone, raw.types.TextPlain, raw.types.TextSpoiler, raw.types.TextStrike, raw.types.TextSubscript, raw.types.TextSuperscript, raw.types.TextUnderline, raw.types.TextUrl]
else:
    # noinspection PyRedeclaration
    class RichText(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 29 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            TextAnchor
            TextAutoEmail
            TextAutoPhone
            TextAutoUrl
            TextBankCard
            TextBold
            TextBotCommand
            TextCashtag
            TextConcat
            TextCustomEmoji
            TextDate
            TextEmail
            TextEmpty
            TextFixed
            TextHashtag
            TextImage
            TextItalic
            TextMarked
            TextMath
            TextMention
            TextMentionName
            TextPhone
            TextPlain
            TextSpoiler
            TextStrike
            TextSubscript
            TextSuperscript
            TextUnderline
            TextUrl
        """

        QUALNAME = "pyrogram.raw.base.RichText"
        __union_types__ = Union[raw.types.TextAnchor, raw.types.TextAutoEmail, raw.types.TextAutoPhone, raw.types.TextAutoUrl, raw.types.TextBankCard, raw.types.TextBold, raw.types.TextBotCommand, raw.types.TextCashtag, raw.types.TextConcat, raw.types.TextCustomEmoji, raw.types.TextDate, raw.types.TextEmail, raw.types.TextEmpty, raw.types.TextFixed, raw.types.TextHashtag, raw.types.TextImage, raw.types.TextItalic, raw.types.TextMarked, raw.types.TextMath, raw.types.TextMention, raw.types.TextMentionName, raw.types.TextPhone, raw.types.TextPlain, raw.types.TextSpoiler, raw.types.TextStrike, raw.types.TextSubscript, raw.types.TextSuperscript, raw.types.TextUnderline, raw.types.TextUrl]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/rich-text"
            )
