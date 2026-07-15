#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    SentCodeType = Union[raw.types.auth.SentCodeTypeApp, raw.types.auth.SentCodeTypeCall, raw.types.auth.SentCodeTypeEmailCode, raw.types.auth.SentCodeTypeFirebaseSms, raw.types.auth.SentCodeTypeFlashCall, raw.types.auth.SentCodeTypeFragmentSms, raw.types.auth.SentCodeTypeMissedCall, raw.types.auth.SentCodeTypeSetUpEmailRequired, raw.types.auth.SentCodeTypeSms, raw.types.auth.SentCodeTypeSmsPhrase, raw.types.auth.SentCodeTypeSmsWord]
else:
    # noinspection PyRedeclaration
    class SentCodeType(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 11 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.SentCodeTypeApp
            auth.SentCodeTypeCall
            auth.SentCodeTypeEmailCode
            auth.SentCodeTypeFirebaseSms
            auth.SentCodeTypeFlashCall
            auth.SentCodeTypeFragmentSms
            auth.SentCodeTypeMissedCall
            auth.SentCodeTypeSetUpEmailRequired
            auth.SentCodeTypeSms
            auth.SentCodeTypeSmsPhrase
            auth.SentCodeTypeSmsWord
        """

        QUALNAME = "pyrogram.raw.base.auth.SentCodeType"
        __union_types__ = Union[raw.types.auth.SentCodeTypeApp, raw.types.auth.SentCodeTypeCall, raw.types.auth.SentCodeTypeEmailCode, raw.types.auth.SentCodeTypeFirebaseSms, raw.types.auth.SentCodeTypeFlashCall, raw.types.auth.SentCodeTypeFragmentSms, raw.types.auth.SentCodeTypeMissedCall, raw.types.auth.SentCodeTypeSetUpEmailRequired, raw.types.auth.SentCodeTypeSms, raw.types.auth.SentCodeTypeSmsPhrase, raw.types.auth.SentCodeTypeSmsWord]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/sent-code-type"
            )
