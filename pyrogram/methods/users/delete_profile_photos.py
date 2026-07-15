#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional

import pyrogram
from pyrogram import raw, utils
from pyrogram.file_id import FileType


class DeleteProfilePhotos:
    async def delete_profile_photos(
        self: "pyrogram.Client",
        photo_ids: Union[str, list[str]] = None,
        public: bool = False,
        for_my_bot: Union[int, str] = None,
    ) -> bool:
        """Delete your own profile photos.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            photo_ids (``str`` | List of ``str``, *optional*):
                A single :obj:`~pyrogram.types.Photo` id as string or multiple ids as list of strings for deleting
                more than one photos at once.
                If not specified, the most recent profile photo of the user would be deleted.

            public (``bool``, *optional*):
                Pass True to upload a public profile photo for users who are restricted from viewing your real profile photos due to your privacy settings.
                Defaults to False.

            for_my_bot (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the bot for which profile photo has to be updated instead of the current user.
                The bot should have ``can_be_edited`` property set to True.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Get the photos to be deleted
                photos = [p async for p in app.get_chat_photos("me")]

                # Delete one photo
                await app.delete_profile_photos(photos[0].file_id)

                # Delete the rest of the photos
                await app.delete_profile_photos([p.file_id for p in photos[1:]])

                # Delete one photo without fetching the current profile photos of the user
                await app.delete_profile_photos()
        """
        if photo_ids is None:
            return bool(
                await self.invoke(
                    raw.functions.photos.UpdateProfilePhoto(
                        id=raw.types.InputPhotoEmpty(),
                        fallback=public,
                        bot=await self.resolve_peer(for_my_bot) if for_my_bot else None,
                    )
                )
            )

        photo_ids = photo_ids if isinstance(photo_ids, list) else [photo_ids]
        input_photos = [utils.get_input_media_from_file_id(i, FileType.PHOTO).id for i in photo_ids]

        return bool(
            await self.invoke(
                raw.functions.photos.DeletePhotos(
                    id=input_photos
                )
            )
        )
