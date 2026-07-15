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


class UpdateStarGiftAuctionUserState(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``DC58F31E``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

        user_state (:obj:`StarGiftAuctionUserState <pyrogram.raw.base.StarGiftAuctionUserState>`):
            N/A

    """

    __slots__: list[str] = ["gift_id", "user_state"]

    ID = 0xdc58f31e
    QUALNAME = "types.UpdateStarGiftAuctionUserState"

    def __init__(self, *, gift_id: int, user_state: "raw.base.StarGiftAuctionUserState") -> None:
        self.gift_id = gift_id  # long
        self.user_state = user_state  # StarGiftAuctionUserState

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarGiftAuctionUserState":
        # No flags
        
        gift_id = Long.read(b)
        
        user_state = TLObject.read(b)
        
        return UpdateStarGiftAuctionUserState(gift_id=gift_id, user_state=user_state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.gift_id))
        
        b.write(self.user_state.write())
        
        return b.getvalue()
