#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types
from ..object import Object


class InlineKeyboardMarkup(Object):
    """An inline keyboard that appears right next to the message it belongs to.

    Parameters:
        inline_keyboard (List of List of :obj:`~pyrogram.types.InlineKeyboardButton`):
            List of button rows, each represented by a List of InlineKeyboardButton objects.

    """

    def __init__(self, inline_keyboard: list[list["types.InlineKeyboardButton"]]):
        super().__init__()

        self.inline_keyboard = inline_keyboard

    @staticmethod
    def read(o):
        inline_keyboard = []

        for i in o.rows:
            row = []

            for j in i.buttons:
                row.append(types.InlineKeyboardButton.read(j))

            inline_keyboard.append(row)

        return InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard
        )

    async def write(self, client: "pyrogram.Client"):
        rows = []

        for r in self.inline_keyboard:
            buttons = []

            for b in r:
                buttons.append(await b.write(client))

            rows.append(raw.types.KeyboardButtonRow(buttons=buttons))

        return raw.types.ReplyInlineMarkup(rows=rows)

        # There seems to be a Python issues with nested async comprehensions.
        # See: https://bugs.python.org/issue33346
        #
        # return raw.types.ReplyInlineMarkup(
        #     rows=[raw.types.KeyboardButtonRow(
        #         buttons=[await j.write(client) for j in i]
        #     ) for i in self.inline_keyboard]
        # )
