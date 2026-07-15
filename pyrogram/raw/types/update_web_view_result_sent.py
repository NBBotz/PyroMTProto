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


class UpdateWebViewResultSent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``1592B79D``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["query_id"]

    ID = 0x1592b79d
    QUALNAME = "types.UpdateWebViewResultSent"

    def __init__(self, *, query_id: int) -> None:
        self.query_id = query_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebViewResultSent":
        # No flags
        
        query_id = Long.read(b)
        
        return UpdateWebViewResultSent(query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        return b.getvalue()
