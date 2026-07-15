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


class TransferStarGift(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``7F18176A``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

        to_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = ["stargift", "to_id"]

    ID = 0x7f18176a
    QUALNAME = "functions.payments.TransferStarGift"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", to_id: "raw.base.InputPeer") -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.to_id = to_id  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TransferStarGift":
        # No flags
        
        stargift = TLObject.read(b)
        
        to_id = TLObject.read(b)
        
        return TransferStarGift(stargift=stargift, to_id=to_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stargift.write())
        
        b.write(self.to_id.write())
        
        return b.getvalue()
