#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import logging
from typing import Optional

import pyrogram
from pyrogram import raw
from .input_message_content import InputMessageContent

log = logging.getLogger(__name__)


class InputContactMessageContent(InputMessageContent):
    """Content of a contact message to be sent as the result of an inline query.

    Parameters:
        phone_number (``str``):
            Phone number of the user.

        first_name (``str``):
            First name of the user; 1-64 characters.

        last_name (``str``, *optional*):
            Last name of the user; 0-64 characters.

        vcard (``str``, *optional*):
            Additional data about the user in a form of `vCard <https://en.wikipedia.org/wiki/VCard>`_; 0-2048 bytes in length.

    """

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None
    ):
        super().__init__()

        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    async def write(self, client: "pyrogram.Client", reply_markup):
        return raw.types.InputBotInlineMessageMediaContact(
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
            vcard=self.vcard,
            reply_markup=await reply_markup.write(client) if reply_markup else None
        )
