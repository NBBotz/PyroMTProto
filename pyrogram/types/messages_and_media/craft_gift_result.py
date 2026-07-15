#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from pyrogram import types

from ..object import Object


class CraftGiftResult(Object):
    """Contains result of gift crafting.

    It can be one of:

    - :obj:`~pyrogram.types.CraftGiftResultSuccess`
    - :obj:`~pyrogram.types.CraftGiftResultFail`
    """

    def __init__(self):
        super().__init__()


class CraftGiftResultSuccess(CraftGiftResult):
    """Craft was successful.

    Parameters:
        gift (:obj:`~pyrogram.types.Gift`):
            The created gift.
    """

    def __init__(
        self,
        gift: "types.Gift"
    ):
        super().__init__()

        self.gift = gift


class CraftGiftResultFail(CraftGiftResult):
    """Craft has failed."""

    def __init__(self):
        super().__init__()

