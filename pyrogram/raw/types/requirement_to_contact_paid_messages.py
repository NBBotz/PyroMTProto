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


class RequirementToContactPaidMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RequirementToContact`.

    Details:
        - Layer: ``227``
        - ID: ``B4F67E93``

    Parameters:
        stars_amount (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            users.GetRequirementsToContact
    """

    __slots__: list[str] = ["stars_amount"]

    ID = 0xb4f67e93
    QUALNAME = "types.RequirementToContactPaidMessages"

    def __init__(self, *, stars_amount: int) -> None:
        self.stars_amount = stars_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequirementToContactPaidMessages":
        # No flags
        
        stars_amount = Long.read(b)
        
        return RequirementToContactPaidMessages(stars_amount=stars_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.stars_amount))
        
        return b.getvalue()
