#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import io
import os
from typing import Union, Optional

import pyrogram
from pyrogram import raw, types, utils
from pyrogram.file_id import FileType


class SetChatPhoto:
    async def set_chat_photo(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        *,
        photo: Union[str, "io.BytesIO"] = None,
        video: Union[str, "io.BytesIO"] = None,
        photo_frame_start_timestamp: float = None,
        cover: Union[str, "io.BytesIO"] = None,
        cover_start_timestamp: float = None,
    ) -> Union["types.Message", bool]:
        """Set a new chat photo, video or cover photo.

        Upgraded in PyroMTProto to support the ``cover`` parameter added
        in Telegram Layer 227, which sets a separate video/image shown on
        the channel's profile page (distinct from the round avatar).

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            photo (``str`` | :obj:`io.BytesIO`, *optional*):
                New chat photo. Pass a file_id, local file path, or binary
                file-like object.

            video (``str`` | :obj:`io.BytesIO`, *optional*):
                New animated chat photo (H.264/MPEG-4 AVC, max 5 seconds).
                Mutually exclusive with ``photo``.

            photo_frame_start_timestamp (``float``, *optional*):
                UNIX timestamp of the video frame to use as static preview.
                Only used when ``video`` is set.

            cover (``str`` | :obj:`io.BytesIO`, *optional*):
                Cover photo/video for the channel profile page.
                Can be a file path, binary object, or existing file_id.
                **New in Layer 227** — only for channels/supergroups.

            cover_start_timestamp (``float``, *optional*):
                UNIX timestamp of the video frame to use as static cover preview.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: Service message on success,
            or True if no message was returned.

        Example:
            .. code-block:: python

                # Set photo
                await app.set_chat_photo(chat_id, photo="photo.jpg")

                # Set video avatar
                await app.set_chat_photo(chat_id, video="avatar.mp4")

                # Set cover photo (Layer 227+, channels only)
                await app.set_chat_photo(chat_id, cover="cover.jpg")

                # Set both avatar and cover together
                await app.set_chat_photo(
                    chat_id,
                    photo="avatar.jpg",
                    cover="cover.jpg"
                )
        """
        peer = await self.resolve_peer(chat_id)

        # Build uploaded cover file (if provided)
        cover_file = None
        if cover is not None:
            if isinstance(cover, str) and not os.path.isfile(cover):
                # It's a file_id
                cover_input = utils.get_input_media_from_file_id(cover, FileType.PHOTO)
                cover_file = raw.types.InputChatPhoto(id=cover_input.id)
            else:
                # Upload the cover file
                uploaded_cover = await self.save_file(cover)
                cover_file = raw.types.InputChatUploadedPhoto(
                    file=uploaded_cover,
                    video_start_ts=cover_start_timestamp,
                )

        # Build main photo/video
        if photo is not None or video is not None:
            if isinstance(photo, str) and photo and not os.path.isfile(photo):
                # photo is a file_id
                photo_input = utils.get_input_media_from_file_id(photo, FileType.PHOTO)
                chat_photo = raw.types.InputChatPhoto(id=photo_input.id)
            else:
                chat_photo = raw.types.InputChatUploadedPhoto(
                    file=await self.save_file(photo) if photo else None,
                    video=await self.save_file(video) if video else None,
                    video_start_ts=photo_frame_start_timestamp,
                )
        elif cover_file is not None:
            # Only cover was specified — use empty photo for the avatar slot
            chat_photo = raw.types.InputChatPhotoEmpty()
        else:
            raise ValueError("At least one of photo, video, or cover must be provided")

        # Invoke the right RPC
        if isinstance(peer, raw.types.InputPeerChat):
            r = await self.invoke(
                raw.functions.messages.EditChatPhoto(
                    chat_id=peer.chat_id,
                    photo=chat_photo,
                )
            )
        elif isinstance(peer, raw.types.InputPeerChannel):
            # For channels with cover support: two separate EditPhoto calls
            # if both are specified
            if cover_file is not None and (photo is not None or video is not None):
                # First set the main photo
                await self.invoke(
                    raw.functions.channels.EditPhoto(
                        channel=peer,
                        photo=chat_photo
                    )
                )
                # Then set the cover
                r = await self.invoke(
                    raw.functions.channels.EditPhoto(
                        channel=peer,
                        photo=cover_file
                    )
                )
            elif cover_file is not None:
                r = await self.invoke(
                    raw.functions.channels.EditPhoto(
                        channel=peer,
                        photo=cover_file
                    )
                )
            else:
                r = await self.invoke(
                    raw.functions.channels.EditPhoto(
                        channel=peer,
                        photo=chat_photo
                    )
                )
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user')

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
