#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from enum import auto

from .auto_name import AutoName


class ParseMode(AutoName):
    """Parse mode enumeration used in various places to set a specific parse mode"""

    DEFAULT = auto()
    "Default mode. Markdown and HTML combined"

    MARKDOWN = auto()
    "Markdown only mode"

    HTML = auto()
    "HTML only mode"

    DISABLED = auto()
    "Disabled mode"
