#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw, types
from ..object import Object
from ..update import Update


class ManagedBotUpdated(Object, Update):
    """This object contains information about the creation or token update of a bot that is managed by the current bot.

    Parameters:
        user (:obj:`~pyrogram.types.User`, *optional*):
            User that created the bot.
        
        bot (:obj:`~pyrogram.types.User`, *optional*):
            Information about the bot. The bot's token can be fetched using the method :obj:`~pyrogram.raw.functions.bots.CreateBot`.

    """

    def __init__(
        self,
        *,
        user: "types.User",
        bot: "types.User",
    ):
        super().__init__()

        self.user = user
        self.bot = bot

    @staticmethod
    def _parse(
        client,
        update: "raw.types.UpdateManagedBot",
        users: dict,
    ) -> "ManagedBotUpdated":
        return ManagedBotUpdated(
            user=types.User._parse(client, users[update.user_id]),
            bot=types.User._parse(client, users[update.bot_id]),
        )
