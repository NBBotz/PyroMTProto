#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    Difference = Union[raw.types.updates.Difference, raw.types.updates.DifferenceEmpty, raw.types.updates.DifferenceSlice, raw.types.updates.DifferenceTooLong]
else:
    # noinspection PyRedeclaration
    class Difference(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.DifferenceEmpty
            updates.DifferenceSlice
            updates.DifferenceTooLong

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetDifference
        """

        QUALNAME = "pyrogram.raw.base.updates.Difference"
        __union_types__ = Union[raw.types.updates.Difference, raw.types.updates.DifferenceEmpty, raw.types.updates.DifferenceSlice, raw.types.updates.DifferenceTooLong]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/difference"
            )
