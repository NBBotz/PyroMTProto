#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class VideoChatStarted(Object):
    """A service message about a voice chat started in the chat.

    Currently holds no information.
    """

    def __init__(self):
        super().__init__()
