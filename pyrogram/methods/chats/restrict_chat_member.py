#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime
from typing import Union

import pyrogram
from pyrogram import raw, utils
from pyrogram import types


class RestrictChatMember:
    async def restrict_chat_member(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
        permissions: "types.ChatPermissions",
        use_independent_chat_permissions: bool = False,
        until_date: datetime = utils.zero_datetime()
    ) -> "types.Chat":
        """Restrict a user in a supergroup.

        You must be an administrator in the supergroup for this to work and must have the appropriate admin rights.
        Pass True for all permissions to lift restrictions from a user.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            permissions (:obj:`~pyrogram.types.ChatPermissions`):
                New user permissions.

            use_independent_chat_permissions (``bool``, *optional*):
                Pass True if chat permissions are set independently.
                Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will
                imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions;
                the can_send_polls permission will imply the can_send_messages permission.

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                from datetime import datetime, timedelta
                from pyrogram.types import ChatPermissions

                # Completely restrict chat member (mute) forever
                await app.restrict_chat_member(chat_id, user_id, ChatPermissions())

                # Chat member muted for 24h
                await app.restrict_chat_member(chat_id, user_id, ChatPermissions(),
                    datetime.now() + timedelta(days=1))

                # Chat member can only send text messages
                await app.restrict_chat_member(chat_id, user_id,
                    ChatPermissions(can_send_messages=True))
        """
        r = await self.invoke(
            raw.functions.channels.EditBanned(
                channel=await self.resolve_peer(chat_id),
                participant=await self.resolve_peer(user_id),
                banned_rights=permissions.write(
                    use_independent_chat_permissions,
                    until_date
                )
            )
        )

        return types.Chat._parse_chat(self, r.chats[0])
