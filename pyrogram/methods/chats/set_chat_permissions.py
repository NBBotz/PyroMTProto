#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class SetChatPermissions:
    async def set_chat_permissions(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        permissions: "types.ChatPermissions",
        use_independent_chat_permissions: bool = False,
    ) -> "types.Chat":
        """Set default chat permissions for all members.

        You must be an administrator in the group or a supergroup for this to work and must have the
        *can_restrict_members* admin rights.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            permissions (:obj:`~pyrogram.types.ChatPermissions`):
                New default chat permissions.

            use_independent_chat_permissions (``bool``, *optional*):
                Pass True if chat permissions are set independently.
                Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will
                imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions;
                the can_send_polls permission will imply the can_send_messages permission.

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                from pyrogram.types import ChatPermissions

                # Completely restrict chat
                await app.set_chat_permissions(chat_id, ChatPermissions())

                # Chat members can only send text messages and media messages
                await app.set_chat_permissions(
                    chat_id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True
                    )
                )
        """

        r = await self.invoke(
            raw.functions.messages.EditChatDefaultBannedRights(
                peer=await self.resolve_peer(chat_id),
                banned_rights=permissions.write(use_independent_chat_permissions)
            )
        )

        return types.Chat._parse_chat(self, r.chats[0])
