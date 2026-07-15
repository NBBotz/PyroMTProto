#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime
from typing import Optional

import pyrogram
from pyrogram import raw
from pyrogram import utils
from ..object import Object


class EmojiStatus(Object):
    """A user emoji status.

    Parameters:
        custom_emoji_id (``str``):
            Custom emoji id.

        until_date (:py:obj:`~datetime.datetime`, *optional*):
            Valid until date.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        custom_emoji_id: str,
        until_date: Optional[datetime] = None,
        _raw: "raw.base.EmojiStatus" = None,
    ):
        super().__init__(client)

        self.custom_emoji_id = custom_emoji_id
        self.until_date = until_date
        self._raw = _raw

    @staticmethod
    def _parse(client, emoji_status: "raw.base.EmojiStatus") -> Optional["EmojiStatus"]:
        if isinstance(emoji_status, raw.types.EmojiStatus):
            return EmojiStatus(
                client=client,
                custom_emoji_id=str(emoji_status.document_id),
                until_date=utils.timestamp_to_datetime(emoji_status.until),
                _raw=emoji_status
            )

        if isinstance(emoji_status, raw.types.EmojiStatusCollectible):
            return EmojiStatus(
                client=client,
                custom_emoji_id=str(emoji_status.document_id),
                until_date=utils.timestamp_to_datetime(emoji_status.until),
                _raw=emoji_status
            )

        return None

    def write(self):
        if self.until_date:
            return raw.types.EmojiStatusUntil(
                document_id=int(self.custom_emoji_id),
                until=utils.datetime_to_timestamp(self.until_date)
            )

        return raw.types.EmojiStatus(
            document_id=int(self.custom_emoji_id)
        )
