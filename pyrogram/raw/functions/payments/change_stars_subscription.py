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


class ChangeStarsSubscription(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``C7770878``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        subscription_id (``str``):
            N/A

        canceled (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["peer", "subscription_id", "canceled"]

    ID = 0xc7770878
    QUALNAME = "functions.payments.ChangeStarsSubscription"

    def __init__(self, *, peer: "raw.base.InputPeer", subscription_id: str, canceled: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.subscription_id = subscription_id  # string
        self.canceled = canceled  # flags.0?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeStarsSubscription":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        subscription_id = String.read(b)
        
        canceled = Bool.read(b) if flags & (1 << 0) else None
        return ChangeStarsSubscription(peer=peer, subscription_id=subscription_id, canceled=canceled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.canceled is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.subscription_id))
        
        if self.canceled is not None:
            b.write(Bool(self.canceled))
        
        return b.getvalue()
