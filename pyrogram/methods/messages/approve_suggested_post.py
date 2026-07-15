#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime
from typing import Union, Optional

import pyrogram
from pyrogram import raw, types, utils


class ApproveSuggestedPost:
    async def approve_suggested_post(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        schedule_date: Optional[datetime] = None,
    ) -> "types.Message":
        """Approve a suggested post in a channel.

        When a user sends a suggested post to a channel where they are not
        an admin, the channel owner/admins can approve or reject it using
        this method.

        You must be an administrator in the channel with the appropriate rights.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel.

            message_id (``int``):
                Identifier of the message containing the suggested post.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date and time when the post should be published.
                Pass None to publish immediately upon approval.

        Returns:
            :obj:`~pyrogram.types.Message`: The approved/published message.

        Raises:
            RPCError: In case of a Telegram RPC error.

        Example:
            .. code-block:: python

                # Approve immediately
                await app.approve_suggested_post(chat_id="@mychannel", message_id=123)

                # Approve and schedule for a specific time
                from datetime import datetime, timezone, timedelta
                future = datetime.now(timezone.utc) + timedelta(hours=2)
                await app.approve_suggested_post("@mychannel", 123, schedule_date=future)
        """
        peer = await self.resolve_peer(chat_id)

        schedule_ts = None
        if schedule_date:
            schedule_ts = int(schedule_date.timestamp())

        r = await self.invoke(
            raw.functions.messages.ToggleSuggestedPostApproval(
                peer=peer,
                msg_id=message_id,
                reject=False,
                schedule_date=schedule_ts,
            )
        )

        for update in r.updates:
            if isinstance(update, (raw.types.UpdateNewMessage, raw.types.UpdateNewChannelMessage)):
                return await types.Message._parse(
                    self,
                    update.message,
                    {u.id: u for u in r.users},
                    {c.id: c for c in r.chats},
                    replies=self.fetch_replies
                )

        return True
