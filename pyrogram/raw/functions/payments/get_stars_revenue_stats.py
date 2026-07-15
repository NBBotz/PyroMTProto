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


class GetStarsRevenueStats(TLObject["raw.base.payments.StarsRevenueStats"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``D91FFAD6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        dark (``bool``, *optional*):
            N/A

        ton (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsRevenueStats <pyrogram.raw.base.payments.StarsRevenueStats>`
    """

    __slots__: list[str] = ["peer", "dark", "ton"]

    ID = 0xd91ffad6
    QUALNAME = "functions.payments.GetStarsRevenueStats"

    def __init__(self, *, peer: "raw.base.InputPeer", dark: Optional[bool] = None, ton: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.dark = dark  # flags.0?true
        self.ton = ton  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsRevenueStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        ton = True if flags & (1 << 1) else False
        peer = TLObject.read(b)
        
        return GetStarsRevenueStats(peer=peer, dark=dark, ton=ton)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        flags |= (1 << 1) if self.ton else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
