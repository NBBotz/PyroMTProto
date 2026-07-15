#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional, AsyncGenerator
import pyrogram
from pyrogram import raw, types


class GetUserGifts:
    async def get_user_gifts(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        offset: str = "",
        limit: int = 100,
    ) -> AsyncGenerator["types.Gift", None]:
        """Get gifts saved in a user's profile.

        Parameters:
            user_id (``int`` | ``str``):
                User whose gifts to retrieve.

            offset (``str``, *optional*):
                Pagination offset from a previous call's ``next_offset``.

            limit (``int``, *optional*):
                Maximum number of gifts to return. Defaults to 100.

        Yields:
            :obj:`~pyrogram.types.Gift`: Each gift in the user's collection.

        Example:
            .. code-block:: python

                async for gift in app.get_user_gifts("username"):
                    print(gift.id, gift.stars)
        """
        peer = await self.resolve_peer(user_id)

        while True:
            r = await self.invoke(
                raw.functions.payments.GetSavedStarGifts(
                    peer=peer,
                    offset=offset,
                    limit=min(limit, 100),
                )
            )

            users = {u.id: u for u in r.users}
            chats = {c.id: c for c in r.chats}

            for gift in r.gifts:
                parsed = types.Gift._parse(self, gift, users, chats)
                if parsed:
                    yield parsed
                    limit -= 1
                    if limit == 0:
                        return

            if not r.next_offset:
                break
            offset = r.next_offset
