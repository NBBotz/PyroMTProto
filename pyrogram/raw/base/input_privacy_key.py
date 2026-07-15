#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    InputPrivacyKey = Union[raw.types.InputPrivacyKeyAbout, raw.types.InputPrivacyKeyAddedByPhone, raw.types.InputPrivacyKeyBirthday, raw.types.InputPrivacyKeyChatInvite, raw.types.InputPrivacyKeyForwards, raw.types.InputPrivacyKeyNoPaidMessages, raw.types.InputPrivacyKeyPhoneCall, raw.types.InputPrivacyKeyPhoneNumber, raw.types.InputPrivacyKeyPhoneP2P, raw.types.InputPrivacyKeyProfilePhoto, raw.types.InputPrivacyKeySavedMusic, raw.types.InputPrivacyKeyStarGiftsAutoSave, raw.types.InputPrivacyKeyStatusTimestamp, raw.types.InputPrivacyKeyVoiceMessages]
else:
    # noinspection PyRedeclaration
    class InputPrivacyKey(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 14 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPrivacyKeyAbout
            InputPrivacyKeyAddedByPhone
            InputPrivacyKeyBirthday
            InputPrivacyKeyChatInvite
            InputPrivacyKeyForwards
            InputPrivacyKeyNoPaidMessages
            InputPrivacyKeyPhoneCall
            InputPrivacyKeyPhoneNumber
            InputPrivacyKeyPhoneP2P
            InputPrivacyKeyProfilePhoto
            InputPrivacyKeySavedMusic
            InputPrivacyKeyStarGiftsAutoSave
            InputPrivacyKeyStatusTimestamp
            InputPrivacyKeyVoiceMessages
        """

        QUALNAME = "pyrogram.raw.base.InputPrivacyKey"
        __union_types__ = Union[raw.types.InputPrivacyKeyAbout, raw.types.InputPrivacyKeyAddedByPhone, raw.types.InputPrivacyKeyBirthday, raw.types.InputPrivacyKeyChatInvite, raw.types.InputPrivacyKeyForwards, raw.types.InputPrivacyKeyNoPaidMessages, raw.types.InputPrivacyKeyPhoneCall, raw.types.InputPrivacyKeyPhoneNumber, raw.types.InputPrivacyKeyPhoneP2P, raw.types.InputPrivacyKeyProfilePhoto, raw.types.InputPrivacyKeySavedMusic, raw.types.InputPrivacyKeyStarGiftsAutoSave, raw.types.InputPrivacyKeyStatusTimestamp, raw.types.InputPrivacyKeyVoiceMessages]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/input-privacy-key"
            )
