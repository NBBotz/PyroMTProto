#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class InputStoryContent(Object):
    """This object describes the content of a story to post.

    Currently, it can be one of:

    - :obj:`~pyrogram.types.InputStoryContentPhoto`
    - :obj:`~pyrogram.types.InputStoryContentVideo`
    """

    def __init__(self):
        super().__init__()
