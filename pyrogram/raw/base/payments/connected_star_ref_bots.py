#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    ConnectedStarRefBots = Union[raw.types.payments.ConnectedStarRefBots]
else:
    # noinspection PyRedeclaration
    class ConnectedStarRefBots(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.ConnectedStarRefBots

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetConnectedStarRefBots
            payments.GetConnectedStarRefBot
            payments.ConnectStarRefBot
            payments.EditConnectedStarRefBot
        """

        QUALNAME = "pyrogram.raw.base.payments.ConnectedStarRefBots"
        __union_types__ = Union[raw.types.payments.ConnectedStarRefBots]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/connected-star-ref-bots"
            )
