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


class FinishTakeoutSession(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``1D2652EE``

    Parameters:
        success (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["success"]

    ID = 0x1d2652ee
    QUALNAME = "functions.account.FinishTakeoutSession"

    def __init__(self, *, success: Optional[bool] = None) -> None:
        self.success = success  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FinishTakeoutSession":
        
        flags = Int.read(b)
        
        success = True if flags & (1 << 0) else False
        return FinishTakeoutSession(success=success)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.success else 0
        b.write(Int(flags))
        
        return b.getvalue()
