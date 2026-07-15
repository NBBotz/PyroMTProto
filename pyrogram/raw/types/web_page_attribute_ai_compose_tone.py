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


class WebPageAttributeAiComposeTone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``227``
        - ID: ``7781FE18``

    Parameters:
        emoji_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["emoji_id"]

    ID = 0x7781fe18
    QUALNAME = "types.WebPageAttributeAiComposeTone"

    def __init__(self, *, emoji_id: int) -> None:
        self.emoji_id = emoji_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeAiComposeTone":
        # No flags
        
        emoji_id = Long.read(b)
        
        return WebPageAttributeAiComposeTone(emoji_id=emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.emoji_id))
        
        return b.getvalue()
