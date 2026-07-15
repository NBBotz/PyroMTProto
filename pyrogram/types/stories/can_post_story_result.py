#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class CanPostStoryResult(Object):
    """This object represents result of checking whether the current user can post a story on behalf of the specific chat.

    Currently, it can be one of:

    - :obj:`~pyrogram.types.CanPostStoryResultOk`
    - :obj:`~pyrogram.types.CanPostStoryResultPremiumNeeded`
    - :obj:`~pyrogram.types.CanPostStoryResultBoostNeeded`
    - :obj:`~pyrogram.types.CanPostStoryResultActiveStoryLimitExceeded`
    - :obj:`~pyrogram.types.CanPostStoryResultWeeklyLimitExceeded`
    - :obj:`~pyrogram.types.CanPostStoryResultMonthlyLimitExceeded`
    """

    def __init__(self):
        super().__init__()
