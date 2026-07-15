#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import types
from ..object import Object


class UsersShared(Object):
    """This object contains information about the users whose identifiers were shared with the bot using a :obj:`~pyrogram.types.KeyboardButtonRequestUsers` button.

    Parameters:
        request_id (``int``):
            Identifier of the request.

        users (List of :obj:`~pyrogram.types.User`):
            Information about users shared with the bot.

    """

    def __init__(
        self,
        *,
        request_id: int,
        users: list["types.User"]
    ):
        super().__init__()

        self.request_id = request_id
        self.users = users
