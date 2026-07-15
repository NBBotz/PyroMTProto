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


class WebPageAttributeUniqueStarGift(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``227``
        - ID: ``CF6F6DB8``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

    """

    __slots__: list[str] = ["gift"]

    ID = 0xcf6f6db8
    QUALNAME = "types.WebPageAttributeUniqueStarGift"

    def __init__(self, *, gift: "raw.base.StarGift") -> None:
        self.gift = gift  # StarGift

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeUniqueStarGift":
        # No flags
        
        gift = TLObject.read(b)
        
        return WebPageAttributeUniqueStarGift(gift=gift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.gift.write())
        
        return b.getvalue()
