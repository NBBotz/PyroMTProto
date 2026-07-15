#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import types
from ..object import Object


class KeyboardButtonRequestManagedBot(Object):
    """This object defines the parameters for the creation of a managed bot.
    Information about the created bot will be shared with the bot using the update managed_bot and a Message with the field ``managed_bot_created``.

    Parameters:
        request_id (``int``):
            Signed 32-bit identifier of the request. Must be unique within the message

        suggested_name (``str``, *optional*):
            Suggested name for the bot.

        suggested_username (``str``, *optional*):
            Suggested username for the bot.

    """
    def __init__(
        self,
        request_id: int,
        suggested_name: str = None,
        suggested_username: str = None,
    ):
        self.request_id = request_id
        self.suggested_name = suggested_name
        self.suggested_username = suggested_username
