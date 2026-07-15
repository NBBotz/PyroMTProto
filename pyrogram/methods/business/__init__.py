#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .answer_shipping_query import AnswerShippingQuery
from .create_invoice_link import CreateInvoiceLink
from .get_available_gifts import GetAvailableGifts
from .get_business_connection import GetBusinessConnection
from .get_collectible_item_info import GetCollectibleItemInfo
from .get_owned_star_count import GetOwnedStarCount
from .get_payment_form import GetPaymentForm
from .refund_star_payment import RefundStarPayment
from .send_invoice import SendInvoice
from .send_payment_form import SendPaymentForm

# Business Account management (new in PyroMTProto)
from .update_business_intro import UpdateBusinessIntro
from .update_business_location import UpdateBusinessLocation
from .update_business_work_hours import UpdateBusinessWorkHours
from .update_business_away_message import UpdateBusinessAwayMessage
from .update_business_greeting_message import UpdateBusinessGreetingMessage

# Business Chat Links (new in PyroMTProto)
from .get_business_chat_links import GetBusinessChatLinks
from .create_business_chat_link import CreateBusinessChatLink
from .delete_business_chat_link import DeleteBusinessChatLink
from .edit_business_chat_link import EditBusinessChatLink
from .resolve_business_chat_link import ResolveBusinessChatLink

from .delete_business_messages import DeleteBusinessMessages
from .get_business_account_gifts import GetBusinessAccountGifts
from .get_business_account_star_balance import GetBusinessAccountStarBalance
from .get_connected_bots import GetConnectedBots
from .transfer_business_account_stars import TransferBusinessAccountStars

class Business(
    AnswerPreCheckoutQuery,
    AnswerShippingQuery,
    CreateInvoiceLink,
    GetAvailableGifts,
    GetBusinessConnection,
    GetCollectibleItemInfo,
    GetOwnedStarCount,
    GetPaymentForm,
    RefundStarPayment,
    SendInvoice,
    SendPaymentForm,
    # Business account management
    UpdateBusinessIntro,
    UpdateBusinessLocation,
    UpdateBusinessWorkHours,
    UpdateBusinessAwayMessage,
    UpdateBusinessGreetingMessage,
    # Business chat links
    GetBusinessChatLinks,
    CreateBusinessChatLink,
    DeleteBusinessChatLink,
    EditBusinessChatLink,
    ResolveBusinessChatLink,
    DeleteBusinessMessages,
    GetBusinessAccountGifts,
    GetBusinessAccountStarBalance,
    GetConnectedBots,
    TransferBusinessAccountStars,
):
    pass
