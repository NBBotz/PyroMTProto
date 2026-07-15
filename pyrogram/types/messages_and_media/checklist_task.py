#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime
from typing import Dict, Optional

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object
from .message import Str


class ChecklistTask(Object):
    """Describes a task in a checklist.

    Parameters:
        id (``int``):
            Unique identifier of the task.

        text (``str``):
            Text of the task.

        text_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities that appear in the task text.
            May contain only Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, Url, EmailAddress, Mention, Hashtag, Cashtag and PhoneNumber entities.

        completed_by_user (:obj:`~pyrogram.types.User`, *optional*):
            User that completed the task.
            omitted if the task wasn't completed by a user.

        completed_by_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Chat that completed the task.
            omitted if the task wasn't completed by a chat.

        completion_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the task was completed.
            None if the task isn't completed.

    """

    def __init__(
        self,
        *,
        id: int,
        text: str,
        text_entities: Optional[list["types.MessageEntity"]] = None,
        completed_by_user: Optional["types.User"] = None,
        completed_by_chat: Optional["types.Chat"] = None,
        completion_date: Optional[datetime] = None,
    ):
        super().__init__()

        self.id = id
        self.text = text
        self.text_entities = text_entities
        self.completed_by_user = completed_by_user
        self.completed_by_chat = completed_by_chat
        self.completion_date = completion_date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        item: "raw.types.TodoItem",
        completion: "raw.types.TodoCompletion",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"],
    ) -> "ChecklistTask":
        text_entities = [
            types.MessageEntity._parse(client, entity, users)
            for entity in item.title.entities
        ]
        text_entities = types.List(filter(lambda x: x is not None, text_entities))
        text = Str(item.title.text).init(text_entities) or None

        completed_by_peer = getattr(completion, "completed_by", None)
        completed_by_user = None
        completed_by_chat = None
        if completed_by_peer:
            completed_by_peer_id = utils.get_raw_peer_id(completed_by_peer)
            if isinstance(completed_by_peer, raw.types.PeerUser):
                completed_by_user = types.User._parse(client, users.get(completed_by_peer_id))
            else:
                completed_by_chat = types.Chat._parse_chat(client, chats.get(completed_by_peer_id))

        return ChecklistTask(
            id=item.id,
            text=text,
            text_entities=text_entities,
            completed_by_user=completed_by_user,
            completed_by_chat=completed_by_chat,
            completion_date=utils.timestamp_to_datetime(getattr(completion, "date", None))
        )
