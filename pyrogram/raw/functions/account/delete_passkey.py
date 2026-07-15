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


class DeletePasskey(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``F5B5563F``

    Parameters:
        id (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["id"]

    ID = 0xf5b5563f
    QUALNAME = "functions.account.DeletePasskey"

    def __init__(self, *, id: str) -> None:
        self.id = id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePasskey":
        # No flags
        
        id = String.read(b)
        
        return DeletePasskey(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        return b.getvalue()
