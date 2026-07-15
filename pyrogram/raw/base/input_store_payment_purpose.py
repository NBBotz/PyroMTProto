#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    InputStorePaymentPurpose = Union[raw.types.InputStorePaymentAuthCode, raw.types.InputStorePaymentGiftPremium, raw.types.InputStorePaymentPremiumGiftCode, raw.types.InputStorePaymentPremiumGiveaway, raw.types.InputStorePaymentPremiumSubscription, raw.types.InputStorePaymentStarsGift, raw.types.InputStorePaymentStarsGiveaway, raw.types.InputStorePaymentStarsTopup]
else:
    # noinspection PyRedeclaration
    class InputStorePaymentPurpose(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputStorePaymentAuthCode
            InputStorePaymentGiftPremium
            InputStorePaymentPremiumGiftCode
            InputStorePaymentPremiumGiveaway
            InputStorePaymentPremiumSubscription
            InputStorePaymentStarsGift
            InputStorePaymentStarsGiveaway
            InputStorePaymentStarsTopup
        """

        QUALNAME = "pyrogram.raw.base.InputStorePaymentPurpose"
        __union_types__ = Union[raw.types.InputStorePaymentAuthCode, raw.types.InputStorePaymentGiftPremium, raw.types.InputStorePaymentPremiumGiftCode, raw.types.InputStorePaymentPremiumGiveaway, raw.types.InputStorePaymentPremiumSubscription, raw.types.InputStorePaymentStarsGift, raw.types.InputStorePaymentStarsGiveaway, raw.types.InputStorePaymentStarsTopup]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/input-store-payment-purpose"
            )
