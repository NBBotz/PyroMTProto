#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    PrivacyRule = Union[raw.types.PrivacyValueAllowAll, raw.types.PrivacyValueAllowBots, raw.types.PrivacyValueAllowChatParticipants, raw.types.PrivacyValueAllowCloseFriends, raw.types.PrivacyValueAllowContacts, raw.types.PrivacyValueAllowPremium, raw.types.PrivacyValueAllowUsers, raw.types.PrivacyValueDisallowAll, raw.types.PrivacyValueDisallowBots, raw.types.PrivacyValueDisallowChatParticipants, raw.types.PrivacyValueDisallowContacts, raw.types.PrivacyValueDisallowUsers]
else:
    # noinspection PyRedeclaration
    class PrivacyRule(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 12 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PrivacyValueAllowAll
            PrivacyValueAllowBots
            PrivacyValueAllowChatParticipants
            PrivacyValueAllowCloseFriends
            PrivacyValueAllowContacts
            PrivacyValueAllowPremium
            PrivacyValueAllowUsers
            PrivacyValueDisallowAll
            PrivacyValueDisallowBots
            PrivacyValueDisallowChatParticipants
            PrivacyValueDisallowContacts
            PrivacyValueDisallowUsers
        """

        QUALNAME = "pyrogram.raw.base.PrivacyRule"
        __union_types__ = Union[raw.types.PrivacyValueAllowAll, raw.types.PrivacyValueAllowBots, raw.types.PrivacyValueAllowChatParticipants, raw.types.PrivacyValueAllowCloseFriends, raw.types.PrivacyValueAllowContacts, raw.types.PrivacyValueAllowPremium, raw.types.PrivacyValueAllowUsers, raw.types.PrivacyValueDisallowAll, raw.types.PrivacyValueDisallowBots, raw.types.PrivacyValueDisallowChatParticipants, raw.types.PrivacyValueDisallowContacts, raw.types.PrivacyValueDisallowUsers]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/privacy-rule"
            )
