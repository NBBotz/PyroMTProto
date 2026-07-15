#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, types, utils


class SearchChats:
    async def search_chats(
        self: "pyrogram.Client",
        query: str,
        limit: int = 10,
        personalize_result: bool = False
    ) -> list["types.Chat"]:
        """Searches for the specified query in the title and username of already known chats via request to the server.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            query (``str``):
                Query to search for.

            limit (``int``, *optional*):
                The maximum number of chats to be returned. Defaults to 10.

            personalize_result (``bool``, *optional*):
                True, if should return personalized results, else would return all found user identifiers. Defaults to False.

        Returns:
            List of :obj:`~pyrogram.types.Chat`: Returns chats in the order seen in the main chat list

        Example:
            .. code-block:: python

                chats = await app.search_chats("Pyrogram")

        """
        r = await self.invoke(
            raw.functions.contacts.Search(
                q=query,
                limit=limit
            )
        )
        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}
        c = []
        attr = "my_results" if personalize_result else "results"
        m = getattr(r, attr, [])
        for o in m:
            id = utils.get_raw_peer_id(o)
            if isinstance(o, raw.types.PeerUser):
                c.append(
                    types.Chat._parse_chat(
                        self,
                        users[id]
                    )
                )
            else:
                c.append(
                    types.Chat._parse_chat(
                        self,
                        chats[id]
                    )
                )
        return types.List(c)
