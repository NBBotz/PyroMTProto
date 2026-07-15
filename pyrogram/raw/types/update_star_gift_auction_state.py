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


class UpdateStarGiftAuctionState(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``48E246C2``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

        state (:obj:`StarGiftAuctionState <pyrogram.raw.base.StarGiftAuctionState>`):
            N/A

    """

    __slots__: list[str] = ["gift_id", "state"]

    ID = 0x48e246c2
    QUALNAME = "types.UpdateStarGiftAuctionState"

    def __init__(self, *, gift_id: int, state: "raw.base.StarGiftAuctionState") -> None:
        self.gift_id = gift_id  # long
        self.state = state  # StarGiftAuctionState

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarGiftAuctionState":
        # No flags
        
        gift_id = Long.read(b)
        
        state = TLObject.read(b)
        
        return UpdateStarGiftAuctionState(gift_id=gift_id, state=state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.gift_id))
        
        b.write(self.state.write())
        
        return b.getvalue()
