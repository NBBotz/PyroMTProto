#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    ResetPasswordResult = Union[raw.types.account.ResetPasswordFailedWait, raw.types.account.ResetPasswordOk, raw.types.account.ResetPasswordRequestedWait]
else:
    # noinspection PyRedeclaration
    class ResetPasswordResult(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.ResetPasswordFailedWait
            account.ResetPasswordOk
            account.ResetPasswordRequestedWait

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
        """

        QUALNAME = "pyrogram.raw.base.account.ResetPasswordResult"
        __union_types__ = Union[raw.types.account.ResetPasswordFailedWait, raw.types.account.ResetPasswordOk, raw.types.account.ResetPasswordRequestedWait]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/reset-password-result"
            )
