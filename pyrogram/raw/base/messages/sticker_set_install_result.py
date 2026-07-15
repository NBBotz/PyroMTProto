#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    StickerSetInstallResult = Union[raw.types.messages.StickerSetInstallResultArchive, raw.types.messages.StickerSetInstallResultSuccess]
else:
    # noinspection PyRedeclaration
    class StickerSetInstallResult(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.StickerSetInstallResultArchive
            messages.StickerSetInstallResultSuccess

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.InstallStickerSet
        """

        QUALNAME = "pyrogram.raw.base.messages.StickerSetInstallResult"
        __union_types__ = Union[raw.types.messages.StickerSetInstallResultArchive, raw.types.messages.StickerSetInstallResultSuccess]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/sticker-set-install-result"
            )
