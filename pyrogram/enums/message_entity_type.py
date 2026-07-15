#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from enum import auto

from pyrogram import raw

from .auto_name import AutoName


class MessageEntityType(AutoName):
    """Message entity type enumeration used in :obj:`~pyrogram.types.MessageEntity`."""

    MENTION = raw.types.MessageEntityMention
    "``@username``"

    HASHTAG = raw.types.MessageEntityHashtag
    "``#hashtag or #hashtag@PyrogramChat``"

    CASHTAG = raw.types.MessageEntityCashtag
    "``$USD or $USD@PyrogramChat``"

    BOT_COMMAND = raw.types.MessageEntityBotCommand
    "``/start@pyrogrambot``"

    URL = raw.types.MessageEntityUrl
    "``https://pyrogram.org``"

    EMAIL = raw.types.MessageEntityEmail
    "``do-not-reply@pyrogram.org``"

    PHONE_NUMBER = raw.types.MessageEntityPhone
    "``+1-212-555-0123``"

    BOLD = raw.types.MessageEntityBold
    "Bold text"

    ITALIC = raw.types.MessageEntityItalic
    "Italic text"

    UNDERLINE = raw.types.MessageEntityUnderline
    "Underlined text"

    STRIKETHROUGH = raw.types.MessageEntityStrike
    "Strikethrough text"

    SPOILER = raw.types.MessageEntitySpoiler
    "Spoiler message"

    BLOCKQUOTE = auto()
    "Block quotation"

    EXPANDABLE_BLOCKQUOTE = auto()
    "collapsed-by-default block quotation"

    CODE = raw.types.MessageEntityCode
    "Monowidth string"

    PRE = raw.types.MessageEntityPre
    "Monowidth block (see ``language``)"

    TEXT_LINK = raw.types.MessageEntityTextUrl
    "For clickable text URLs (see ``url``)"

    TEXT_MENTION = raw.types.MessageEntityMentionName
    "for users without usernames (see ``user``)"

    CUSTOM_EMOJI = raw.types.MessageEntityCustomEmoji
    "for inline custom emoji stickers (see ``custom_emoji_id``)"

    BANK_CARD = raw.types.MessageEntityBankCard
    "Bank card text"

    DATE_TIME = raw.types.MessageEntityFormattedDate
    "for formatted date and time (see ``unix_time`` and ``date_time_format``)"

    DIFF_TYPE_INSERT = raw.types.MessageEntityDiffInsert
    "Represents a change of a text: Addition of some text"

    DIFF_TYPE_REPLACE = raw.types.MessageEntityDiffReplace
    "Represents a change of a text: Change of some text"

    DIFF_TYPE_DELETE = raw.types.MessageEntityDiffDelete
    "Represents a change of a text: Removal of some text"

    UNKNOWN = raw.types.MessageEntityUnknown
    "Unknown message entity type"
