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


class GetStarsRevenueAdsAccountUrl(TLObject["raw.base.payments.StarsRevenueAdsAccountUrl"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``D1D7EFC5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`payments.StarsRevenueAdsAccountUrl <pyrogram.raw.base.payments.StarsRevenueAdsAccountUrl>`
    """

    __slots__: list[str] = ["peer"]

    ID = 0xd1d7efc5
    QUALNAME = "functions.payments.GetStarsRevenueAdsAccountUrl"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsRevenueAdsAccountUrl":
        # No flags
        
        peer = TLObject.read(b)
        
        return GetStarsRevenueAdsAccountUrl(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()
