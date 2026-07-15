#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import raw, utils
from pyrogram.file_id import FileType


class AddProfileAudio:
    async def add_profile_audio(
        self: "pyrogram.Client",
        audio: str,
    ):
        """Adds an audio file to the beginning of the profile audio files of the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            audio (``str``):
                Audio file to add.
                Pass a file_id as string to add an audio file that exists on the Telegram servers.
                The file must have been uploaded to the server using :meth:`~pyrogram.Client.send_audio`.

        Returns:
            ``bool``: On success, True is returned.
        
        Raises:
            :obj:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.

        Example:
            .. code-block:: python

                # Adds an audio file to a profile
                await app.add_profile_audio(file_id)

        """
        return await self.invoke(
            raw.functions.account.SaveMusic(
                id=(utils.get_input_media_from_file_id(audio, FileType.AUDIO)).id
            )
        )
