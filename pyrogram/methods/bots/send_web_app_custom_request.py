#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw, types


class SendWebAppCustomRequest:
    async def send_web_app_custom_request(
        self: "pyrogram.Client",
        bot_user_id: Union[int, str],
        method: str,
        parameters: str
    ) -> str:
        """Sends a custom request from a Web App.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot_user_id (``int`` | ``str``):
                Unique identifier of the inline bot you want to get results from. You can specify
                a @username (str) or a bot ID (int).

            method (``str``):
                The method name.
            
            parameters (``str``):
                JSON-serialized method parameters.

        Returns:
            ``str``: On success, a JSON-serialized result is returned.

        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        """

        r = await self.invoke(
            raw.functions.bots.InvokeWebViewCustomMethod(
                bot=await self.resolve_peer(bot_user_id),
                custom_method=method,
                params=raw.types.DataJSON(
                    data=parameters
                )
            )
        )

        return r.data
