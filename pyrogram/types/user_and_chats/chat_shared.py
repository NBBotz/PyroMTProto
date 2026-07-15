#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import types
from ..object import Object


class ChatShared(Object):
    """This object contains information about a chat that was shared with the bot using a :obj:`~pyrogram.types.KeyboardButtonRequestChat` button.

    Parameters:
        request_id (``int``):
            Identifier of the request.

        chats (List of :obj:`~pyrogram.types.Chat`):
            Information about chat shared with the bot.

    """

    def __init__(
        self,
        *,
        request_id: int,
        chats: list["types.Chat"]
    ):
        super().__init__()

        self.request_id = request_id
        self.chats = chats
