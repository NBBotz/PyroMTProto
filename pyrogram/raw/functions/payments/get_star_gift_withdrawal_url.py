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


class GetStarGiftWithdrawalUrl(TLObject["raw.base.payments.StarGiftWithdrawalUrl"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``D06E93A8``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

    Returns:
        :obj:`payments.StarGiftWithdrawalUrl <pyrogram.raw.base.payments.StarGiftWithdrawalUrl>`
    """

    __slots__: list[str] = ["stargift", "password"]

    ID = 0xd06e93a8
    QUALNAME = "functions.payments.GetStarGiftWithdrawalUrl"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", password: "raw.base.InputCheckPasswordSRP") -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarGiftWithdrawalUrl":
        # No flags
        
        stargift = TLObject.read(b)
        
        password = TLObject.read(b)
        
        return GetStarGiftWithdrawalUrl(stargift=stargift, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stargift.write())
        
        b.write(self.password.write())
        
        return b.getvalue()
