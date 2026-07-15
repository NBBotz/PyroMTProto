#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING

from ..object import Object

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import types


class Checklist(Object):
    """Represents a native Telegram Checklist (added in Layer 226).

    A checklist is a special message containing a title and a list of
    completable tasks. Users can tick/untick each item.

    Parameters:
        title (``str``):
            The title of the checklist.

        items (``list`` of :obj:`~pyrogram.types.ChecklistTask`):
            The list of items in the checklist.

        others_can_complete (``bool``):
            True if other chat members (not just the creator) can mark items as complete.

        others_can_add (``bool``):
            True if other members can add new items to the checklist.

        completed_count (``int``):
            Number of completed items.

        total_count (``int``):
            Total number of items.
    """

    def __init__(
        self,
        *,
        title: str = "",
        items: list = None,
        others_can_complete: bool = False,
        others_can_add: bool = False,
        completed_count: int = 0,
        total_count: int = 0
    ):
        super().__init__()
        self.title = title
        self.items = items or []
        self.others_can_complete = others_can_complete
        self.others_can_add = others_can_add
        self.completed_count = completed_count
        self.total_count = total_count

    @property
    def completion_percentage(self) -> float:
        """Completion percentage (0.0–100.0)."""
        if not self.total_count:
            return 0.0
        return round(self.completed_count / self.total_count * 100, 1)

    @staticmethod
    def _parse(client: "pyrogram.Client", media, users: dict = None, chats: dict = None) -> "Checklist | None":
        """Parse from raw.types.MessageMediaTodo."""
        from pyrogram import types

        if media is None:
            return None

        # MessageMediaTodo has a .todo field which is raw.types.Todo
        todo = getattr(media, "todo", media)
        flags = getattr(todo, "flags", 0)

        # Parse items - todo.list is the list of TodoItem
        # Completions - todo.completions maps item id → TodoCompletion
        raw_items = getattr(todo, "list", []) or []
        completions_list = getattr(todo, "completions", []) or []
        completions = {getattr(c, "id", None): c for c in completions_list}

        items = [
            types.ChecklistTask._parse(client, item, completions.get(item.id), users or {}, chats or {})
            for item in raw_items
        ]

        completed_count = sum(1 for i in items if i.completion_date is not None)

        return Checklist(
            title=getattr(getattr(todo, "title", None), "text", "") or "",
            items=items,
            others_can_complete=bool(flags & (1 << 0)),
            others_can_add=bool(flags & (1 << 1)),
            completed_count=completed_count,
            total_count=len(items)
        )
