#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .input_paid_media import InputPaidMedia
from .input_paid_media_photo import InputPaidMediaPhoto
from .input_paid_media_video import InputPaidMediaVideo
from .paid_media_info import PaidMediaInfo
from .paid_media import PaidMedia
from .paid_media_preview import PaidMediaPreview
from .paid_media_photo import PaidMediaPhoto
from .paid_media_video import PaidMediaVideo
from .paid_media_purchased import PaidMediaPurchased

__all__ = [
    "InputPaidMedia",
    "InputPaidMediaPhoto",
    "InputPaidMediaVideo",
    "PaidMediaInfo",
    "PaidMedia",
    "PaidMediaPreview",
    "PaidMediaPhoto",
    "PaidMediaVideo",
    "PaidMediaPurchased",
]
