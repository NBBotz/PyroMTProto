#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram
from pyrogram import types

from ..object import Object
from .paid_media import PaidMedia


class PaidMediaPhoto(PaidMedia):
    """The paid media is a photo.

    Parameters:
        photo (:obj:`~pyrogram.types.Photo`):
            The photo.

    """

    def __init__(
        self,
        *,
        photo: "types.Photo" = None
    ):
        super().__init__()

        self.photo = photo
