#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object

import pyrogram
from pyrogram import raw, types


class PaidReactionType(Object):
    """This object describes the type of paid message reaction.
    
    It can be one of:

    - :obj:`~pyrogram.types.PaidReactionTypeRegular`
    - :obj:`~pyrogram.types.PaidReactionTypeAnonymous`
    - :obj:`~pyrogram.types.PaidReactionTypeChat`

    """

    def __init__(self):
        super().__init__()
    
    async def write(
        self,
        client: "pyrogram.Client",
    ):
        if isinstance(self, PaidReactionTypeChat):
            return self._raw(
                peer=await client.resolve_peer(self.chat_id)
            )
        else:
            return self._raw()



class PaidReactionTypeRegular(PaidReactionType):
    """A paid reaction on behalf of the current user.

    """
    def __init__(self):
        super().__init__()

        self._raw = raw.types.PaidReactionPrivacyDefault


class PaidReactionTypeAnonymous(PaidReactionType):
    """An anonymous paid reaction.
    
    """
    def __init__(self):
        super().__init__()

        self._raw = raw.types.PaidReactionPrivacyAnonymous


class PaidReactionTypeChat(PaidReactionType):
    """A paid reaction on behalf of an owned chat.

    It is intended to be used with :obj:`~pyrogram.Client.`.

    Parameters:
        chat_id (``int``):
            Unique identifier (int) or username (str) of the target chat.
    
    """

    def __init__(self, chat_id: int):
        super().__init__()

        self.chat_id = chat_id
        self._raw = raw.types.PaidReactionPrivacyPeer
