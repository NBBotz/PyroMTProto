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


class InputStarGiftAuction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStarGiftAuction`.

    Details:
        - Layer: ``227``
        - ID: ``2E16C98``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["gift_id"]

    ID = 0x2e16c98
    QUALNAME = "types.InputStarGiftAuction"

    def __init__(self, *, gift_id: int) -> None:
        self.gift_id = gift_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStarGiftAuction":
        # No flags
        
        gift_id = Long.read(b)
        
        return InputStarGiftAuction(gift_id=gift_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.gift_id))
        
        return b.getvalue()
