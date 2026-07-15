#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class BusinessIntro(Object):
    """

    Parameters:
        title (``str``, *optional*):
            Title text of the business intro
        
        message (``str``, *optional*):
            Message text of the business intro

        sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
            Sticker of the business intro

    """

    def __init__(
        self,
        *,
        title: str = None,
        message: str = None,
        sticker: "types.Sticker" = None
    ):
        super().__init__()

        self.title = title
        self.message = message
        self.sticker = sticker


    @staticmethod
    async def _parse(
        client,
        business_intro: "raw.types.BusinessIntro"
    ) -> "BusinessIntro":
        doc = getattr(business_intro, "sticker", None)
        sticker = None
        if (
            doc and
            isinstance(doc, raw.types.Document)
        ):
            attributes = {type(i): i for i in doc.attributes}
            sticker = await types.Sticker._parse(
                client,
                doc,
                attributes
            )
        return BusinessIntro(
            title=getattr(business_intro, "title", None),
            message=getattr(business_intro, "description", None),
            sticker=sticker
        )
