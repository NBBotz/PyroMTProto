#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import pyrogram

from pyrogram import types
from ..object import Object


class MessageAutoDeleteTimerChanged(Object):
    """This object represents a service message about a change in auto-delete timer settings.

    Parameters:
        message_auto_delete_time (``int``):
            New auto-delete time for messages in the chat; in seconds.
        
        from_user (:obj:`~pyrogram.types.User`, *optional*):
            If set, the chat TTL setting was set not due to a manual change by one of participants, but automatically because one of the participants has the default TTL settings enabled.

    """

    def __init__(
        self,
        *,
        message_auto_delete_time: int = None,
        from_user: "types.User" = None
    ):
        super().__init__()

        self.message_auto_delete_time = message_auto_delete_time
        self.from_user = from_user
