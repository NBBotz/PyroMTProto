#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from enum import auto

from .auto_name import AutoName


class ClientPlatform(AutoName):
    """Valid platforms for a :obj:`~pyrogram.Client`."""

    ANDROID = auto()
    "Android"

    IOS = auto()
    "iOS"

    WP = auto()
    "Windows Phone"

    BB = auto()
    "Blackberry"

    DESKTOP = auto()
    "Desktop"

    WEB = auto()
    "Web"

    UBP = auto()
    "Ubuntu Phone"

    OTHER = auto()
    "Other"
