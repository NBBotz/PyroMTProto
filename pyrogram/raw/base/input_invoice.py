#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    InputInvoice = Union[raw.types.InputInvoiceBusinessBotTransferStars, raw.types.InputInvoiceChatInviteSubscription, raw.types.InputInvoiceMessage, raw.types.InputInvoicePremiumAuthCode, raw.types.InputInvoicePremiumGiftCode, raw.types.InputInvoicePremiumGiftStars, raw.types.InputInvoiceSlug, raw.types.InputInvoiceStarGift, raw.types.InputInvoiceStarGiftAuctionBid, raw.types.InputInvoiceStarGiftDropOriginalDetails, raw.types.InputInvoiceStarGiftPrepaidUpgrade, raw.types.InputInvoiceStarGiftResale, raw.types.InputInvoiceStarGiftTransfer, raw.types.InputInvoiceStarGiftUpgrade, raw.types.InputInvoiceStars]
else:
    # noinspection PyRedeclaration
    class InputInvoice(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 15 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputInvoiceBusinessBotTransferStars
            InputInvoiceChatInviteSubscription
            InputInvoiceMessage
            InputInvoicePremiumAuthCode
            InputInvoicePremiumGiftCode
            InputInvoicePremiumGiftStars
            InputInvoiceSlug
            InputInvoiceStarGift
            InputInvoiceStarGiftAuctionBid
            InputInvoiceStarGiftDropOriginalDetails
            InputInvoiceStarGiftPrepaidUpgrade
            InputInvoiceStarGiftResale
            InputInvoiceStarGiftTransfer
            InputInvoiceStarGiftUpgrade
            InputInvoiceStars
        """

        QUALNAME = "pyrogram.raw.base.InputInvoice"
        __union_types__ = Union[raw.types.InputInvoiceBusinessBotTransferStars, raw.types.InputInvoiceChatInviteSubscription, raw.types.InputInvoiceMessage, raw.types.InputInvoicePremiumAuthCode, raw.types.InputInvoicePremiumGiftCode, raw.types.InputInvoicePremiumGiftStars, raw.types.InputInvoiceSlug, raw.types.InputInvoiceStarGift, raw.types.InputInvoiceStarGiftAuctionBid, raw.types.InputInvoiceStarGiftDropOriginalDetails, raw.types.InputInvoiceStarGiftPrepaidUpgrade, raw.types.InputInvoiceStarGiftResale, raw.types.InputInvoiceStarGiftTransfer, raw.types.InputInvoiceStarGiftUpgrade, raw.types.InputInvoiceStars]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/input-invoice"
            )
