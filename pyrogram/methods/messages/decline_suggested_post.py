#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional

import pyrogram
from pyrogram import raw


class DeclineSuggestedPost:
    async def decline_suggested_post(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        comment: Optional[str] = None,
    ) -> bool:
        """Decline (reject) a suggested post in a channel.

        The original submitter will receive a notification that their post
        was not approved, optionally with a reason comment.

        You must be an administrator in the channel with appropriate rights.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel.

            message_id (``int``):
                Identifier of the message containing the suggested post.

            comment (``str``, *optional*):
                Rejection reason to send to the post author.
                Maximum 255 characters.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Decline without a reason
                await app.decline_suggested_post("@mychannel", 123)

                # Decline with a reason message to the author
                await app.decline_suggested_post(
                    "@mychannel", 123,
                    comment="The post does not match our channel's topic."
                )
        """
        peer = await self.resolve_peer(chat_id)

        await self.invoke(
            raw.functions.messages.ToggleSuggestedPostApproval(
                peer=peer,
                msg_id=message_id,
                reject=True,
                reject_comment=comment,
            )
        )

        return True
