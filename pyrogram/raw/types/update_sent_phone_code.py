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


class UpdateSentPhoneCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``504AA18F``

    Parameters:
        sent_code (:obj:`auth.SentCode <pyrogram.raw.base.auth.SentCode>`):
            N/A

    """

    __slots__: list[str] = ["sent_code"]

    ID = 0x504aa18f
    QUALNAME = "types.UpdateSentPhoneCode"

    def __init__(self, *, sent_code: "raw.base.auth.SentCode") -> None:
        self.sent_code = sent_code  # auth.SentCode

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSentPhoneCode":
        # No flags
        
        sent_code = TLObject.read(b)
        
        return UpdateSentPhoneCode(sent_code=sent_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.sent_code.write())
        
        return b.getvalue()
