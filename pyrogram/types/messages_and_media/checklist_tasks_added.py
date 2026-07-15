#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Dict

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ChecklistTasksAdded(Object):
    """Describes a service message about tasks added to a checklist.

    Parameters:
        checklist_message_id (``int``):
            Identifier of the message with the checklist.
            Can be None if the message was deleted.

        tasks (List of :obj:`~pyrogram.types.ChecklistTask`):
            List of tasks added to the checklist.

    """

    def __init__(
        self,
        *,
        checklist_message_id: int,
        tasks: list["types.ChecklistTask"]
    ):

        super().__init__()

        self.checklist_message_id = checklist_message_id
        self.tasks = tasks

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message: "raw.types.MessageService",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"],
    ) -> "ChecklistTasksAdded":
        action: "raw.types.MessageActionTodoAppendTasks" = message.action

        return ChecklistTasksAdded(
            checklist_message_id=getattr(message.reply_to, "reply_to_msg_id", None),
            tasks=types.List([types.ChecklistTask._parse(client, task, None, users, chats) for task in action.list])
        )
