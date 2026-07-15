#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw

from ..object import Object


class ChecklistTasksDone(Object):
    """Describes a service message about checklist tasks marked as done or not done.

    Parameters:
        checklist_message_id (``int``):
            Identifier of the message with the checklist.
            Can be None if the message was deleted.

        marked_as_done_task_ids (List of ``int``):
            Identifiers of tasks that were marked as done.

        marked_as_not_done_task_ids (List of ``int``):
            Identifiers of tasks that were marked as not done.

    """

    def __init__(
        self,
        *,
        checklist_message_id: int,
        marked_as_done_task_ids: list[int],
        marked_as_not_done_task_ids: list[int]
    ):

        super().__init__()

        self.checklist_message_id = checklist_message_id
        self.marked_as_done_task_ids = marked_as_done_task_ids
        self.marked_as_not_done_task_ids = marked_as_not_done_task_ids

    @staticmethod
    def _parse(client: "pyrogram.Client", message: "raw.types.MessageService") -> "ChecklistTasksDone":
        action: "raw.types.MessageActionTodoCompletions" = message.action

        return ChecklistTasksDone(
            checklist_message_id=getattr(message.reply_to, "reply_to_msg_id", None),
            marked_as_done_task_ids=action.completed,
            marked_as_not_done_task_ids=action.incompleted
        )
