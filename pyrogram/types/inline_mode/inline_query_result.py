#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from uuid import uuid4

import pyrogram
from pyrogram import types
from ..object import Object


class InlineQueryResult(Object):
    """This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:

    - :obj:`~pyrogram.types.InlineQueryResultCachedAudio`
    - :obj:`~pyrogram.types.InlineQueryResultCachedDocument`
    - :obj:`~pyrogram.types.InlineQueryResultCachedAnimation`
    - :obj:`~pyrogram.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyrogram.types.InlineQueryResultCachedSticker`
    - :obj:`~pyrogram.types.InlineQueryResultCachedVideo`
    - :obj:`~pyrogram.types.InlineQueryResultCachedVoice`
    - :obj:`~pyrogram.types.InlineQueryResultArticle`
    - :obj:`~pyrogram.types.InlineQueryResultAudio`
    - :obj:`~pyrogram.types.InlineQueryResultContact`
    - :obj:`~pyrogram.types.InlineQueryResultGame`
    - :obj:`~pyrogram.types.InlineQueryResultDocument`
    - :obj:`~pyrogram.types.InlineQueryResultAnimation`
    - :obj:`~pyrogram.types.InlineQueryResultLocation`
    - :obj:`~pyrogram.types.InlineQueryResultPhoto`
    - :obj:`~pyrogram.types.InlineQueryResultVenue`
    - :obj:`~pyrogram.types.InlineQueryResultVideo`
    - :obj:`~pyrogram.types.InlineQueryResultVoice`

    .. note::

        All URLs passed in inline query results will be available to end users and therefore must be assumed to be *public*.

    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "pyrogram.Client"):
        pass
