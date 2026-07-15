#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .advanced import Advanced
from .auth import Auth
from .bots import Bots
from .chats import Chats
from .chat_topics import ChatTopics
from .contacts import Contacts
from .decorators import Decorators
from .invite_links import InviteLinks
from .messages import Messages
from .password import Password
from .phone import Phone
from .stickers import Stickers
from .stories import Stories
from .users import Users
from .utilities import Utilities
from .account import Account
from .business import TelegramBusiness
from .gifts import Gifts
from .payments import Payments
from .premium import Premium


class Methods(
    Account,
    Decorators,
    Advanced,
    Auth,
    Bots,
    Chats,
    ChatTopics,
    Contacts,
    Gifts,
    InviteLinks,
    Messages,
    Password,
    Payments,
    Phone,
    Premium,
    Stickers,
    Stories,
    TelegramBusiness,
    Users,
    Utilities,
):
    pass
