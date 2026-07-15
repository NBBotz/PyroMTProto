#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class StoryOrigin(Object):
    """Contains information about the origin of a story that was reposted.

    Currently, it can be one of:

    - :obj:`~pyrogram.types.StoryOriginPublicStory`
    - :obj:`~pyrogram.types.StoryOriginHiddenUser`

    """

    def __init__(self):
        super().__init__()
