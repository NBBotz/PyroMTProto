#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .send_gift import SendGift
from .get_user_gifts import GetUserGifts
from .save_gift import SaveGift
from .convert_gift import ConvertGift
from .upgrade_gift import UpgradeGift
from .transfer_gift import TransferGift
from .get_gift_upgrade_preview import GetGiftUpgradePreview


class Gifts(
    SendGift,
    GetUserGifts,
    SaveGift,
    ConvertGift,
    UpgradeGift,
    TransferGift,
    GetGiftUpgradePreview,
):
    pass
