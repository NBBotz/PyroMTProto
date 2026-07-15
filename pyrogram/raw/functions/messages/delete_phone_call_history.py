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


class DeletePhoneCallHistory(TLObject["raw.base.messages.AffectedFoundMessages"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``F9CBE409``

    Parameters:
        revoke (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.AffectedFoundMessages <pyrogram.raw.base.messages.AffectedFoundMessages>`
    """

    __slots__: list[str] = ["revoke"]

    ID = 0xf9cbe409
    QUALNAME = "functions.messages.DeletePhoneCallHistory"

    def __init__(self, *, revoke: Optional[bool] = None) -> None:
        self.revoke = revoke  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePhoneCallHistory":
        
        flags = Int.read(b)
        
        revoke = True if flags & (1 << 0) else False
        return DeletePhoneCallHistory(revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke else 0
        b.write(Int(flags))
        
        return b.getvalue()
