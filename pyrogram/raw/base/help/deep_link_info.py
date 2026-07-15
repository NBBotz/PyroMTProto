#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    DeepLinkInfo = Union[raw.types.help.DeepLinkInfo, raw.types.help.DeepLinkInfoEmpty]
else:
    # noinspection PyRedeclaration
    class DeepLinkInfo(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.DeepLinkInfo
            help.DeepLinkInfoEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetDeepLinkInfo
        """

        QUALNAME = "pyrogram.raw.base.help.DeepLinkInfo"
        __union_types__ = Union[raw.types.help.DeepLinkInfo, raw.types.help.DeepLinkInfoEmpty]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/deep-link-info"
            )
