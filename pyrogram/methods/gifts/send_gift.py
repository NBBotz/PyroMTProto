#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional
import pyrogram
from pyrogram import raw, types, enums


class SendGift:
    async def send_gift(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        gift_id: int,
        text: Optional[str] = None,
        parse_mode: "enums.ParseMode" = None,
        hide_sender: bool = False,
    ) -> bool:
        """Send a Telegram Star Gift to a user.

        Parameters:
            user_id (``int`` | ``str``):
                Target user's ID or username.

            gift_id (``int``):
                ID of the star gift to send (from :meth:`get_available_gifts`).

            text (``str``, *optional*):
                A personalised message to include with the gift (max 255 chars).

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Parse mode for the gift message text.

            hide_sender (``bool``, *optional*):
                Pass True to send the gift anonymously. Defaults to False.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                gifts = await app.get_available_gifts()
                await app.send_gift(
                    user_id="username",
                    gift_id=gifts.gifts[0].id,
                    text="Happy Birthday! 🎂"
                )
        """
        peer = await self.resolve_peer(user_id)

        text_message, entities = await self.parser.parse(text or "", parse_mode)

        await self.invoke(
            raw.functions.payments.SendStarGift(
                user_id=peer,
                gift=raw.types.InputStarGiftId(id=gift_id),
                message=raw.types.TextWithEntities(
                    text=text_message,
                    entities=entities or []
                ) if text_message else None,
                hide_name=hide_sender,
            )
        )
        return True
