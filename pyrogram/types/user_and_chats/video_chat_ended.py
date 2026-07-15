#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import raw
from ..object import Object


class VideoChatEnded(Object):
    """A service message about a voice chat ended in the chat.

    Parameters:
        duration (``int``):
            Voice chat duration; in seconds.
    """

    def __init__(
        self, *,
        duration: int
    ):
        super().__init__()

        self.duration = duration

    @staticmethod
    def _parse(action: "raw.types.MessageActionGroupCall") -> "VideoChatEnded":
        return VideoChatEnded(duration=action.duration)
