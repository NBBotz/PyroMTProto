#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import types, raw


class GetVideoChatRtmpUrl:
    async def get_video_chat_rtmp_url(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        replace: bool = False
    ) -> "types.RtmpUrl":
        """Returns RTMP URL for streaming to the chat; requires owner privileges.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat. A chat can be either a basic group, supergroup or a channel.

            replace (``bool``, *optional*):
                Whether to replace the previous stream key or simply return the existing one. Defaults to False, i.e., return the existing one.

        Returns:
            :obj:`~pyrogram.types.RtmpUrl`: On success, the RTMP URL and stream key is returned.

        Example:
            .. code-block:: python

                await app.get_stream_rtmp_url(chat_id)

        """
        peer = await self.resolve_peer(chat_id)

        if not isinstance(peer, (raw.types.InputPeerChat, raw.types.InputPeerChannel)):
            raise ValueError("Target chat should be group, supergroup or channel.")

        r = await self.invoke(
            raw.functions.phone.GetGroupCallStreamRtmpUrl(
                peer=peer,
                revoke=replace
            )
        )

        return types.RtmpUrl._parse(r)
