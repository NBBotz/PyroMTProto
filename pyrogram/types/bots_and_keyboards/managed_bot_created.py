#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw, types
from ..object import Object


class ManagedBotCreated(Object):
    """This object represents a service message about the bot that was created to be managed by the current bot.

    Parameters:
        bot (:obj:`~pyrogram.types.User`, *optional*):
            Information about the bot. The bot's token can be fetched using the method :obj:`~pyrogram.raw.functions.bots.CreateBot`.

    """

    def __init__(
        self,
        *,
        bot: "types.User",
    ):
        super().__init__()

        self.bot = bot

    @staticmethod
    def _parse(
        client,
        action: "raw.types.MessageActionManagedBotCreated",
        users: dict,
    ) -> "ManagedBotCreated":
        return ManagedBotCreated(
            bot=types.User._parse(client, users[action.bot_id]),
        )
