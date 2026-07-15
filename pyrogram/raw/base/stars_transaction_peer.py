#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    StarsTransactionPeer = Union[raw.types.StarsTransactionPeer, raw.types.StarsTransactionPeerAPI, raw.types.StarsTransactionPeerAds, raw.types.StarsTransactionPeerAppStore, raw.types.StarsTransactionPeerFragment, raw.types.StarsTransactionPeerPlayMarket, raw.types.StarsTransactionPeerPremiumBot, raw.types.StarsTransactionPeerUnsupported]
else:
    # noinspection PyRedeclaration
    class StarsTransactionPeer(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarsTransactionPeer
            StarsTransactionPeerAPI
            StarsTransactionPeerAds
            StarsTransactionPeerAppStore
            StarsTransactionPeerFragment
            StarsTransactionPeerPlayMarket
            StarsTransactionPeerPremiumBot
            StarsTransactionPeerUnsupported
        """

        QUALNAME = "pyrogram.raw.base.StarsTransactionPeer"
        __union_types__ = Union[raw.types.StarsTransactionPeer, raw.types.StarsTransactionPeerAPI, raw.types.StarsTransactionPeerAds, raw.types.StarsTransactionPeerAppStore, raw.types.StarsTransactionPeerFragment, raw.types.StarsTransactionPeerPlayMarket, raw.types.StarsTransactionPeerPremiumBot, raw.types.StarsTransactionPeerUnsupported]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/stars-transaction-peer"
            )
