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


class CheckCanSendGiftResultFail(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.CheckCanSendGiftResult`.

    Details:
        - Layer: ``227``
        - ID: ``D5E58274``

    Parameters:
        reason (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CheckCanSendGift
    """

    __slots__: list[str] = ["reason"]

    ID = 0xd5e58274
    QUALNAME = "types.payments.CheckCanSendGiftResultFail"

    def __init__(self, *, reason: "raw.base.TextWithEntities") -> None:
        self.reason = reason  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckCanSendGiftResultFail":
        # No flags
        
        reason = TLObject.read(b)
        
        return CheckCanSendGiftResultFail(reason=reason)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.reason.write())
        
        return b.getvalue()
