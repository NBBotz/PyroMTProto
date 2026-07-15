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


class WebPageAttributeStarGiftAuction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``227``
        - ID: ``1C641C2``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        end_date (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["gift", "end_date"]

    ID = 0x1c641c2
    QUALNAME = "types.WebPageAttributeStarGiftAuction"

    def __init__(self, *, gift: "raw.base.StarGift", end_date: int) -> None:
        self.gift = gift  # StarGift
        self.end_date = end_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStarGiftAuction":
        # No flags
        
        gift = TLObject.read(b)
        
        end_date = Int.read(b)
        
        return WebPageAttributeStarGiftAuction(gift=gift, end_date=end_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.gift.write())
        
        b.write(Int(self.end_date))
        
        return b.getvalue()
