#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types


class GetForumTopicIconStickers:
    async def get_forum_topic_icon_stickers(
        self: "pyrogram.Client"
    ) -> list["types.Sticker"]:
        """Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user.

        .. include:: /_includes/usable-by/users-bots.rst

        Returns:
            List of :obj:`~pyrogram.types.Sticker`: On success, a list of sticker objects is returned.
        """
        r, _ = await self._get_raw_stickers(
            raw.types.InputStickerSetEmojiDefaultTopicIcons()
        )
        return r
