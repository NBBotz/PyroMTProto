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


class InputMessageCallbackQuery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMessage`.

    Details:
        - Layer: ``227``
        - ID: ``ACFA1A7E``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["id", "query_id"]

    ID = 0xacfa1a7e
    QUALNAME = "types.InputMessageCallbackQuery"

    def __init__(self, *, id: int, query_id: int) -> None:
        self.id = id  # int
        self.query_id = query_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageCallbackQuery":
        # No flags
        
        id = Int.read(b)
        
        query_id = Long.read(b)
        
        return InputMessageCallbackQuery(id=id, query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(Long(self.query_id))
        
        return b.getvalue()
