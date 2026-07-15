#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union

import pyrogram
from pyrogram import raw, utils, types
from pyrogram.file_id import FileType

from ..object import Object


class InputPollOption(Object):
    """This object contains information about one answer option in a poll to send.

    Parameters:
        text (:obj:`~pyrogram.types.FormattedText`):
            Option text, 1-100 characters after entity parsing.
            Only custom emoji entities are allowed to be added and only by Premium users.

        media (:obj:`~pyrogram.types.InputMediaPhoto` | :obj:`~pyrogram.types.InputMediaVideo` | :obj:`~pyrogram.types.InputMediaSticker` | :obj:`~pyrogram.types.Location`, *optional*):
            Media associated with the option.
            Currently supports only photo, video, sticker or location.

    """

    def __init__(
        self,
        *,
        text: "types.FormattedText",
        media: Optional[
            Union[
                "types.InputMediaPhoto",
                "types.InputMediaVideo",
                "types.InputMediaSticker",
                "types.Location",
            ]
        ] = None,
    ):
        super().__init__()

        self.text = text
        self.media = media

    async def write(
        self,
        client: "pyrogram.Client",
    ) -> "raw.types.PollAnswer":
        if isinstance(self.text, str):
            self.text = types.FormattedText(text=self.text)

        if self.media is not None and not isinstance(
            self.media,
            (
                types.InputMediaPhoto,
                types.InputMediaVideo,
                types.InputMediaSticker,
                types.Location,
            ),
        ):
            raise ValueError(f"Unsupported media type: {type(self.media)}")
        media = None
        if self.media:
            if isinstance(self.media, types.Location):
                media = await self.media.write()
            else:
                media, _ = await self.media.write(client=client)
        return raw.types.InputPollAnswer(
            text=await self.text.write(client),
            media=media,
        )
