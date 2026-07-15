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


class GetStarsRevenueWithdrawalUrl(TLObject["raw.base.payments.StarsRevenueWithdrawalUrl"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``2433DC92``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

        ton (``bool``, *optional*):
            N/A

        amount (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsRevenueWithdrawalUrl <pyrogram.raw.base.payments.StarsRevenueWithdrawalUrl>`
    """

    __slots__: list[str] = ["peer", "password", "ton", "amount"]

    ID = 0x2433dc92
    QUALNAME = "functions.payments.GetStarsRevenueWithdrawalUrl"

    def __init__(self, *, peer: "raw.base.InputPeer", password: "raw.base.InputCheckPasswordSRP", ton: Optional[bool] = None, amount: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.password = password  # InputCheckPasswordSRP
        self.ton = ton  # flags.0?true
        self.amount = amount  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsRevenueWithdrawalUrl":
        
        flags = Int.read(b)
        
        ton = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        amount = Long.read(b) if flags & (1 << 1) else None
        password = TLObject.read(b)
        
        return GetStarsRevenueWithdrawalUrl(peer=peer, password=password, ton=ton, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        flags |= (1 << 1) if self.amount is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.amount is not None:
            b.write(Long(self.amount))
        
        b.write(self.password.write())
        
        return b.getvalue()
