#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class CopyTextButton(Object):
    """This object represents an inline keyboard button that copies specified text to the clipboard.

    Parameters:
        text (``str``):
            The text to be copied to the clipboard; 1-256 characters.

    """

    def __init__(
        self, *,
        text: str = "",
    ):
        super().__init__()

        self.text = text
