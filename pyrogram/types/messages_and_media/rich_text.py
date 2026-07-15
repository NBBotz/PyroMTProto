#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0
#
#  Rich Text Support — high-level builder for Telegram-formatted messages
#  with full entity coverage including diff types (Layer 227).

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Union
import pyrogram
from pyrogram import raw
from pyrogram.enums import MessageEntityType


# ── Entity dataclass ──────────────────────────────────────────────────

@dataclass
class TextEntity:
    """A formatting entity applied to a range of text.

    Parameters:
        type (:obj:`~pyrogram.enums.MessageEntityType`):
            The type of formatting.

        offset (``int``):
            UTF-16 offset of the entity start.

        length (``int``):
            UTF-16 length of the entity.

        url (``str``, *optional*):
            URL for ``TEXT_LINK`` entities.

        user (:obj:`~pyrogram.types.User`, *optional*):
            User for ``MENTION_NAME`` entities.

        language (``str``, *optional*):
            Programming language for ``PRE`` code blocks.

        custom_emoji_id (``int``, *optional*):
            Document ID for ``CUSTOM_EMOJI`` entities.

        collapsed (``bool``, *optional*):
            If True, blockquote is expandable (collapsed by default).

        unix_time (``int``, *optional*):
            Timestamp for ``DATE_TIME`` entities.
    """
    type: MessageEntityType
    offset: int
    length: int
    url: Optional[str] = None
    user: Optional[object] = None
    language: Optional[str] = None
    custom_emoji_id: Optional[int] = None
    collapsed: bool = False
    unix_time: Optional[int] = None

    def to_raw(self):
        """Convert to a raw TL MessageEntity."""
        t = self.type
        kwargs = dict(offset=self.offset, length=self.length)

        if t == MessageEntityType.BOLD:
            return raw.types.MessageEntityBold(**kwargs)
        elif t == MessageEntityType.ITALIC:
            return raw.types.MessageEntityItalic(**kwargs)
        elif t == MessageEntityType.UNDERLINE:
            return raw.types.MessageEntityUnderline(**kwargs)
        elif t == MessageEntityType.STRIKETHROUGH:
            return raw.types.MessageEntityStrike(**kwargs)
        elif t == MessageEntityType.SPOILER:
            return raw.types.MessageEntitySpoiler(**kwargs)
        elif t == MessageEntityType.CODE:
            return raw.types.MessageEntityCode(**kwargs)
        elif t == MessageEntityType.PRE:
            return raw.types.MessageEntityPre(language=self.language or "", **kwargs)
        elif t == MessageEntityType.BLOCKQUOTE:
            return raw.types.MessageEntityBlockquote(collapsed=self.collapsed, **kwargs)
        elif t == MessageEntityType.TEXT_LINK:
            return raw.types.MessageEntityTextUrl(url=self.url or "", **kwargs)
        elif t == MessageEntityType.MENTION_NAME:
            return raw.types.InputMessageEntityMentionName(
                user_id=self.user, **kwargs
            )
        elif t == MessageEntityType.CUSTOM_EMOJI:
            return raw.types.MessageEntityCustomEmoji(
                document_id=self.custom_emoji_id or 0, **kwargs
            )
        elif t == MessageEntityType.DIFF_TYPE_INSERT:
            return raw.types.MessageEntityDiffInsert(**kwargs)
        elif t == MessageEntityType.DIFF_TYPE_DELETE:
            return raw.types.MessageEntityDiffDelete(**kwargs)
        elif t == MessageEntityType.DIFF_TYPE_REPLACE:
            return raw.types.MessageEntityDiffReplace(**kwargs)
        elif t == MessageEntityType.DATE_TIME:
            return raw.types.MessageEntityFormattedDate(
                unix_time=self.unix_time or 0, **kwargs
            )
        else:
            return raw.types.MessageEntityUnknown(**kwargs)


# ── RichText builder ─────────────────────────────────────────────────

class RichText:
    """High-level builder for Telegram rich text with full entity support.

    Build formatted messages programmatically without writing HTML or Markdown.
    Supports all entity types including diff types (Layer 227) and custom emoji.

    Usage::

        from pyrogram.types import RichText

        rt = (
            RichText()
            .text("Hello, ")
            .bold("World")
            .text("! ")
            .italic("This is italic")
            .text(".\\n")
            .code("print('hello')")
            .text("\\n")
            .blockquote("This is a quote", expandable=True)
        )

        await app.send_message("me", **rt.to_message_kwargs())

    Diff entity example::

        diff = (
            RichText()
            .text("Changes: ")
            .diff_insert("added text")
            .text(" | ")
            .diff_delete("removed text")
            .text(" | ")
            .diff_replace("changed text")
        )
    """

    def __init__(self, text: str = "", entities: list[TextEntity] = None):
        self._text = text
        self._entities: list[TextEntity] = entities or []

    def _add(self, segment: str, entity_type: Optional[MessageEntityType] = None, **kwargs) -> "RichText":
        """Append a text segment with optional formatting."""
        # Calculate UTF-16 offset correctly
        offset = len(self._text.encode("utf-16-le")) // 2
        self._text += segment
        length = len(segment.encode("utf-16-le")) // 2

        if entity_type is not None and length > 0:
            self._entities.append(TextEntity(
                type=entity_type,
                offset=offset,
                length=length,
                **kwargs
            ))
        return self

    # ── Plain text ─────────────────────────────────────────────────

    def text(self, value: str) -> "RichText":
        """Append plain (unformatted) text."""
        return self._add(value)

    def newline(self, count: int = 1) -> "RichText":
        """Append one or more newlines."""
        return self._add("\n" * count)

    # ── Basic formatting ───────────────────────────────────────────

    def bold(self, value: str) -> "RichText":
        """Append **bold** text."""
        return self._add(value, MessageEntityType.BOLD)

    def italic(self, value: str) -> "RichText":
        """Append *italic* text."""
        return self._add(value, MessageEntityType.ITALIC)

    def underline(self, value: str) -> "RichText":
        """Append __underlined__ text."""
        return self._add(value, MessageEntityType.UNDERLINE)

    def strikethrough(self, value: str) -> "RichText":
        """Append ~~strikethrough~~ text."""
        return self._add(value, MessageEntityType.STRIKETHROUGH)

    def spoiler(self, value: str) -> "RichText":
        """Append ||spoiler|| text."""
        return self._add(value, MessageEntityType.SPOILER)

    # ── Code ───────────────────────────────────────────────────────

    def code(self, value: str) -> "RichText":
        """Append inline `code`."""
        return self._add(value, MessageEntityType.CODE)

    def pre(self, value: str, language: str = "") -> "RichText":
        """Append a code block (pre-formatted text).

        Parameters:
            value: The code content.
            language: Programming language for syntax highlighting (e.g. ``"python"``).
        """
        return self._add(value, MessageEntityType.PRE, language=language)

    # ── Blockquote ────────────────────────────────────────────────

    def blockquote(self, value: str, expandable: bool = False) -> "RichText":
        """Append a blockquote.

        Parameters:
            value: The quote text.
            expandable: If True, the blockquote is collapsed and can be expanded.
        """
        return self._add(value, MessageEntityType.BLOCKQUOTE, collapsed=expandable)

    # ── Links ─────────────────────────────────────────────────────

    def link(self, label: str, url: str) -> "RichText":
        """Append a clickable text link.

        Parameters:
            label: Visible link text.
            url: Destination URL.
        """
        return self._add(label, MessageEntityType.TEXT_LINK, url=url)

    def mention(self, name: str, user_id: int) -> "RichText":
        """Append a user mention by name.

        Parameters:
            name: Display name.
            user_id: Telegram user ID.
        """
        return self._add(name, MessageEntityType.MENTION_NAME, user=user_id)

    # ── Custom emoji ──────────────────────────────────────────────

    def emoji(self, placeholder: str, document_id: int) -> "RichText":
        """Append a custom emoji.

        Parameters:
            placeholder: Fallback text (usually the base emoji, e.g. ``"⭐"``).
            document_id: Custom emoji document ID.
        """
        return self._add(placeholder, MessageEntityType.CUSTOM_EMOJI, custom_emoji_id=document_id)

    # ── Diff entities (Layer 227) ──────────────────────────────────

    def diff_insert(self, value: str) -> "RichText":
        """Mark text as an **insertion** (diff highlight, shown in green)."""
        return self._add(value, MessageEntityType.DIFF_TYPE_INSERT)

    def diff_delete(self, value: str) -> "RichText":
        """Mark text as a **deletion** (diff highlight, shown in red)."""
        return self._add(value, MessageEntityType.DIFF_TYPE_DELETE)

    def diff_replace(self, value: str) -> "RichText":
        """Mark text as a **replacement** (diff highlight, shown in yellow/orange)."""
        return self._add(value, MessageEntityType.DIFF_TYPE_REPLACE)

    # ── Timestamp ────────────────────────────────────────────────

    def timestamp(self, display: str, unix_time: int) -> "RichText":
        """Append a formatted date/time entity that shows in the user's local time.

        Parameters:
            display: Fallback display text.
            unix_time: UNIX timestamp.
        """
        return self._add(display, MessageEntityType.DATE_TIME, unix_time=unix_time)

    # ── Combination helpers ───────────────────────────────────────

    def append(self, other: "RichText") -> "RichText":
        """Append another RichText object."""
        offset_shift = len(self._text.encode("utf-16-le")) // 2
        self._text += other._text
        for ent in other._entities:
            self._entities.append(TextEntity(
                type=ent.type,
                offset=ent.offset + offset_shift,
                length=ent.length,
                url=ent.url,
                user=ent.user,
                language=ent.language,
                custom_emoji_id=ent.custom_emoji_id,
                collapsed=ent.collapsed,
                unix_time=ent.unix_time,
            ))
        return self

    # ── Output ───────────────────────────────────────────────────

    @property
    def message_text(self) -> str:
        """The plain text string."""
        return self._text

    @property
    def message_entities(self) -> list[TextEntity]:
        """The list of TextEntity objects."""
        return self._entities

    def to_raw_entities(self) -> list:
        """Convert all entities to raw TL MessageEntity objects."""
        return [e.to_raw() for e in self._entities]

    def to_message_kwargs(self) -> dict:
        """Return kwargs suitable for ``send_message()``.

        Example::

            rt = RichText().bold("Hello!").text(" How are you?")
            await client.send_message("me", **rt.to_message_kwargs())
        """
        return {
            "text": self._text,
            "entities": self._entities,
            "parse_mode": None,  # We're providing entities directly
        }

    def to_caption_kwargs(self) -> dict:
        """Return kwargs suitable for ``send_photo()``, ``send_video()``, etc.

        Example::

            rt = RichText().bold("Photo caption")
            await client.send_photo("me", photo="photo.jpg", **rt.to_caption_kwargs())
        """
        return {
            "caption": self._text,
            "caption_entities": self._entities,
            "parse_mode": None,
        }

    def __repr__(self) -> str:
        return f"RichText(text={self._text!r}, entities={len(self._entities)})"

    def __str__(self) -> str:
        return self._text

    def __add__(self, other: "RichText") -> "RichText":
        result = RichText(self._text, list(self._entities))
        result.append(other)
        return result
