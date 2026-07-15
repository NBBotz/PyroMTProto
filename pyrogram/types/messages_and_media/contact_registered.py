#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class ContactRegistered(Object):
    """A service message that a contact has registered with Telegram.

    Currently holds no information.
    """

    def __init__(self):
        super().__init__()
