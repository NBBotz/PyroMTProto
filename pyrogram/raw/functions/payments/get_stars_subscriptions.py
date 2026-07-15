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


class GetStarsSubscriptions(TLObject["raw.base.payments.StarsStatus"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``32512C5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset (``str``):
            N/A

        missing_balance (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsStatus <pyrogram.raw.base.payments.StarsStatus>`
    """

    __slots__: list[str] = ["peer", "offset", "missing_balance"]

    ID = 0x32512c5
    QUALNAME = "functions.payments.GetStarsSubscriptions"

    def __init__(self, *, peer: "raw.base.InputPeer", offset: str, missing_balance: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset = offset  # string
        self.missing_balance = missing_balance  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsSubscriptions":
        
        flags = Int.read(b)
        
        missing_balance = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        offset = String.read(b)
        
        return GetStarsSubscriptions(peer=peer, offset=offset, missing_balance=missing_balance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.missing_balance else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.offset))
        
        return b.getvalue()
