#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0
#
#  AI Compose Tone methods — new in Layer 227 (aicompose namespace)

from typing import Optional, Union, TYPE_CHECKING

import pyrogram
from pyrogram import raw, types

if TYPE_CHECKING:
    pass


class AICompose:
    async def get_ai_compose_tones(
        self: "pyrogram.Client",
        hash: int = 0
    ) -> list:
        """Get the list of available AI compose tones.

        Available in Layer 227 via the ``aicompose`` TL namespace.
        Tones are used to rewrite/improve text in different styles
        (e.g. formal, casual, shorter, grammar fix, etc.).

        Parameters:
            hash (``int``, *optional*):
                Hash for caching. Pass 0 to always fetch fresh.
                Defaults to 0.

        Returns:
            ``list`` of :obj:`~pyrogram.raw.types.AiComposeTone` objects,
            or empty list if the server returns ``TlNotModified``.

        Example:
            .. code-block:: python

                tones = await app.get_ai_compose_tones()
                for tone in tones:
                    print(tone.slug, tone.emoji_id)
        """
        r = await self.invoke(
            raw.functions.aicompose.GetTones(hash=hash)
        )

        if isinstance(r, raw.types.aicompose.TonesNotModified):
            return []

        # r is raw.types.aicompose.Tones
        return r.tones

    async def get_ai_compose_tone(
        self: "pyrogram.Client",
        tone: Union[str, int]
    ):
        """Get a specific AI compose tone by slug or custom ID.

        Parameters:
            tone (``str`` | ``int``):
                The tone slug (string) or custom tone ID (int).

        Returns:
            :obj:`~pyrogram.raw.types.AiComposeTone` on success.

        Example:
            .. code-block:: python

                tone = await app.get_ai_compose_tone("formal")
                print(tone)
        """
        if isinstance(tone, str):
            tone_input = raw.types.InputAiComposeToneSlug(slug=tone)
        else:
            tone_input = raw.types.InputAiComposeToneId(id=tone)

        return await self.invoke(
            raw.functions.aicompose.GetTone(tone=tone_input)
        )

    async def get_ai_compose_tone_example(
        self: "pyrogram.Client",
        tone: Union[str, int]
    ):
        """Get an example text demonstrating an AI compose tone.

        Parameters:
            tone (``str`` | ``int``):
                The tone slug (string) or custom tone ID (int).

        Returns:
            :obj:`~pyrogram.raw.types.AiComposeToneExample` containing
            ``original_text`` and ``rewritten_text``.

        Example:
            .. code-block:: python

                example = await app.get_ai_compose_tone_example("casual")
                print("Original:", example.original_text)
                print("Rewritten:", example.rewritten_text)
        """
        if isinstance(tone, str):
            tone_input = raw.types.InputAiComposeToneSlug(slug=tone)
        else:
            tone_input = raw.types.InputAiComposeToneId(id=tone)

        return await self.invoke(
            raw.functions.aicompose.GetToneExample(tone=tone_input)
        )

    async def create_ai_compose_tone(
        self: "pyrogram.Client",
        title: str,
        prompt: str,
        emoji_id: Optional[int] = None
    ):
        """Create a custom AI compose tone.

        Only available for users with an active Telegram Premium subscription.

        Parameters:
            title (``str``):
                Display name for the tone (max 32 characters).

            prompt (``str``):
                System prompt that defines how the AI should rewrite text.

            emoji_id (``int``, *optional*):
                Custom emoji document ID to use as the tone icon.

        Returns:
            :obj:`~pyrogram.raw.types.AiComposeTone` with the created tone.

        Example:
            .. code-block:: python

                tone = await app.create_ai_compose_tone(
                    title="Pirate Style",
                    prompt="Rewrite the text in the style of a friendly pirate."
                )
                print("Created tone ID:", tone.id)
        """
        return await self.invoke(
            raw.functions.aicompose.CreateTone(
                title=title,
                prompt=prompt,
                emoji_id=emoji_id
            )
        )

    async def update_ai_compose_tone(
        self: "pyrogram.Client",
        tone_id: int,
        title: Optional[str] = None,
        prompt: Optional[str] = None,
        emoji_id: Optional[int] = None
    ):
        """Update an existing custom AI compose tone.

        Parameters:
            tone_id (``int``):
                ID of the custom tone to update.

            title (``str``, *optional*):
                New display name.

            prompt (``str``, *optional*):
                New system prompt.

            emoji_id (``int``, *optional*):
                New icon emoji document ID.

        Returns:
            ``bool``: True on success.
        """
        await self.invoke(
            raw.functions.aicompose.UpdateTone(
                id=tone_id,
                title=title,
                prompt=prompt,
                emoji_id=emoji_id
            )
        )
        return True

    async def delete_ai_compose_tone(
        self: "pyrogram.Client",
        tone_id: int
    ) -> bool:
        """Delete a custom AI compose tone.

        Parameters:
            tone_id (``int``):
                ID of the custom tone to delete.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_ai_compose_tone(tone_id=123456)
        """
        await self.invoke(
            raw.functions.aicompose.DeleteTone(id=tone_id)
        )
        return True

    async def save_ai_compose_tone(
        self: "pyrogram.Client",
        tone: Union[str, int],
        unsave: bool = False
    ) -> bool:
        """Save or unsave an AI compose tone to your personal list.

        Parameters:
            tone (``str`` | ``int``):
                The tone slug (string) or custom tone ID (int) to save/unsave.

            unsave (``bool``, *optional*):
                Pass True to remove the tone from saved list.
                Defaults to False (saves the tone).

        Returns:
            ``bool``: True on success.
        """
        if isinstance(tone, str):
            tone_input = raw.types.InputAiComposeToneSlug(slug=tone)
        else:
            tone_input = raw.types.InputAiComposeToneId(id=tone)

        await self.invoke(
            raw.functions.aicompose.SaveTone(
                tone=tone_input,
                unsave=unsave
            )
        )
        return True
