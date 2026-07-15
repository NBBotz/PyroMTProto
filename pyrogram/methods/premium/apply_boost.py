#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union
import pyrogram
from pyrogram import raw


class ApplyBoost:
    async def apply_boost(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        slots: list[int] = None,
    ) -> list:
        """Apply your Telegram Premium boost slots to a channel/group.

        Premium users can boost channels to increase their level.
        Each Premium subscription grants a certain number of boost slots.

        Parameters:
            chat_id (``int`` | ``str``):
                Channel or group to boost.

            slots (``list`` of ``int``, *optional*):
                Specific boost slot indices to apply.
                If None, applies all available slots.

        Returns:
            :obj:`~pyrogram.raw.types.premium.MyBoosts` with the updated
            list of your active boosts.

        Example:
            .. code-block:: python

                result = await app.apply_boost("@mychannel")
                print(f"Now boosting {len(result.my_boosts)} channels")

                # Apply only slot 0
                await app.apply_boost("@mychannel", slots=[0])
        """
        peer = await self.resolve_peer(chat_id)

        if slots is None:
            # Get available slots first
            my_boosts = await self.invoke(
                raw.functions.premium.GetMyBoosts()
            )
            slots = [b.slot for b in my_boosts.my_boosts if not b.peer]

        return await self.invoke(
            raw.functions.premium.ApplyBoost(
                peer=peer,
                slots=slots,
            )
        )
