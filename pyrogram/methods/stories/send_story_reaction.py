#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union, Optional
import pyrogram
from pyrogram import raw


class SendStoryReaction:
    async def send_story_reaction(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
        reaction: Optional[Union[str, int]] = None,
        add_to_recent: bool = True,
    ) -> bool:
        """Send or remove a reaction on a story.

        Parameters:
            chat_id (``int`` | ``str``):
                Owner of the story (user or channel).

            story_id (``int``):
                ID of the story to react to.

            reaction (``str`` | ``int``, *optional*):
                The reaction to send. Pass an emoji string (e.g. ``"❤️"``)
                for standard reactions, an ``int`` document ID for custom
                emoji reactions, or ``None`` to remove the reaction.

            add_to_recent (``bool``, *optional*):
                If True, add this reaction to your recently used list.
                Defaults to True.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # React with a heart
                await app.send_story_reaction("username", story_id=1, reaction="❤️")

                # Remove reaction
                await app.send_story_reaction("username", story_id=1)
        """
        peer = await self.resolve_peer(chat_id)

        if reaction is None:
            raw_reaction = raw.types.ReactionEmpty()
        elif isinstance(reaction, int):
            raw_reaction = raw.types.ReactionCustomEmoji(document_id=reaction)
        else:
            raw_reaction = raw.types.ReactionEmoji(emoticon=reaction)

        await self.invoke(
            raw.functions.stories.SendReaction(
                peer=peer,
                story_id=story_id,
                reaction=raw_reaction,
                add_to_recent=add_to_recent,
            )
        )
        return True
