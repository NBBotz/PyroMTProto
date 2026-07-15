#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional

from pyrogram import raw, types
from ..object import Object


class MessageEffect(Object):
    """Contains information about an effect added to a message.

    Parameters:
        id (``int`` ``64-bit``, *optional*):
            Unique identifier of the effect.

        emoji (``str``):
            Emoji that represents the effect.

        static_icon (:obj:`~pyrogram.types.Sticker`, *optional*):
            Static icon for the effect in WEBP format; may be null if none

        effect_animation (:obj:`~pyrogram.types.Document`, *optional*):
            Effect animation for the effect in TGS format.

        select_animation (:obj:`~pyrogram.types.Document`, *optional*):
            Select animation for the effect in TGS format.

        is_premium (``bool``, *optional*):
            True, if Telegram Premium subscription is required to use the effect.

    """

    def __init__(
        self,
        *,
        id: int,
        emoji: str,
        static_icon: Optional["types.Sticker"] = None,
        effect_animation: Optional["types.Document"] = None,
        select_animation: Optional["types.Document"] = None,
        is_premium: Optional[bool] = None
    ):
        super().__init__()

        self.id = id
        self.emoji = emoji
        self.static_icon = static_icon
        self.effect_animation = effect_animation
        self.select_animation = select_animation
        self.is_premium = is_premium

    @staticmethod
    async def _parse(
        client,
        effect: "raw.types.AvailableEffect",
        effect_animation_document: "raw.types.Document" = None,
        static_icon_document: "raw.types.Document" = None,
        select_animation_document: "raw.types.Document" = None
    ) -> "MessageEffect":
        effect_animation = None
        static_icon = None
        select_animation = None

        effect_sticker_id = effect.effect_sticker_id
        static_icon_id = getattr(effect, "static_icon_id", None)
        effect_animation_id = getattr(effect, "effect_animation_id", None)

        if effect_animation_document:
            effect_animation = await types.Sticker._parse(
                client,
                effect_animation_document,
                {type(i): i for i in effect_animation_document.attributes}
            )
        # TODO: FIXME!
        if static_icon_document:
            document_attributes = {
                type(i): i for i in static_icon_document.attributes
            }
            file_name = getattr(document_attributes.get(raw.types.DocumentAttributeFilename, None), "file_name", None)
            static_icon = types.Document._parse(
                client,
                static_icon_document,
                file_name
            )
        if select_animation_document:
            document_attributes = {
                type(i): i for i in select_animation_document.attributes
            }
            file_name = getattr(document_attributes.get(raw.types.DocumentAttributeFilename, None), "file_name", None)
            select_animation = types.Document._parse(
                client,
                select_animation_document,
                file_name
            )

        return MessageEffect(
            id=effect.id,
            emoji=effect.emoticon,
            static_icon=static_icon,
            effect_animation=effect_animation,  # TODO: FIXME!
            select_animation=select_animation,  # TODO: FIXME!
            is_premium=getattr(effect, "premium_required", None)
        )
