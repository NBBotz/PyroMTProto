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


class ResolveStarGiftOffer(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``E9CE781C``

    Parameters:
        offer_msg_id (``int`` ``32-bit``):
            N/A

        decline (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = ["offer_msg_id", "decline"]

    ID = 0xe9ce781c
    QUALNAME = "functions.payments.ResolveStarGiftOffer"

    def __init__(self, *, offer_msg_id: int, decline: Optional[bool] = None) -> None:
        self.offer_msg_id = offer_msg_id  # int
        self.decline = decline  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveStarGiftOffer":
        
        flags = Int.read(b)
        
        decline = True if flags & (1 << 0) else False
        offer_msg_id = Int.read(b)
        
        return ResolveStarGiftOffer(offer_msg_id=offer_msg_id, decline=decline)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.decline else 0
        b.write(Int(flags))
        
        b.write(Int(self.offer_msg_id))
        
        return b.getvalue()
