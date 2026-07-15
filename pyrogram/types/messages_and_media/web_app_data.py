#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw
from ..object import Object


class WebAppData(Object):
    """Contains data sent from a `Web App <https://core.telegram.org/bots/webapps>`_ to the bot.

    Parameters:
        data (``str``, *optional*):
            The data. Be aware that a bad client can send arbitrary data in this field.

        button_text (``str``):
            Text of the *web_app* keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.

    """

    def __init__(
        self,
        *,
        data: str,
        button_text: str,
    ):
        super().__init__()

        self.data = data
        self.button_text = button_text

    @staticmethod
    def _parse(action: "raw.types.MessageActionWebViewDataSentMe"):
        return WebAppData(
            data=getattr(action, "data", None),
            button_text=action.text
        )
