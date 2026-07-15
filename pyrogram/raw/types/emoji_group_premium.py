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


class EmojiGroupPremium(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiGroup`.

    Details:
        - Layer: ``227``
        - ID: ``93BCF34``

    Parameters:
        title (``str``):
            N/A

        icon_emoji_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["title", "icon_emoji_id"]

    ID = 0x93bcf34
    QUALNAME = "types.EmojiGroupPremium"

    def __init__(self, *, title: str, icon_emoji_id: int) -> None:
        self.title = title  # string
        self.icon_emoji_id = icon_emoji_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroupPremium":
        # No flags
        
        title = String.read(b)
        
        icon_emoji_id = Long.read(b)
        
        return EmojiGroupPremium(title=title, icon_emoji_id=icon_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Long(self.icon_emoji_id))
        
        return b.getvalue()
