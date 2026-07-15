#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from io import BytesIO
from typing import TYPE_CHECKING, Optional, Any

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject

if TYPE_CHECKING:
    from pyrogram import raw

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetEmojiGameInfo(TLObject["raw.base.messages.EmojiGameInfo"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``FB7E8CA7``

    Parameters:
        No parameters required.

    Returns:
        :obj:`messages.EmojiGameInfo <pyrogram.raw.base.messages.EmojiGameInfo>`
    """

    __slots__: list[str] = []

    ID = 0xfb7e8ca7
    QUALNAME = "functions.messages.GetEmojiGameInfo"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiGameInfo":
        # No flags
        
        return GetEmojiGameInfo()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
