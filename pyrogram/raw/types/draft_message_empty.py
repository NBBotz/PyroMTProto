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


class DraftMessageEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DraftMessage`.

    Details:
        - Layer: ``227``
        - ID: ``1B0C841A``

    Parameters:
        date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["date"]

    ID = 0x1b0c841a
    QUALNAME = "types.DraftMessageEmpty"

    def __init__(self, *, date: Optional[int] = None) -> None:
        self.date = date  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DraftMessageEmpty":
        
        flags = Int.read(b)
        
        date = Int.read(b) if flags & (1 << 0) else None
        return DraftMessageEmpty(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.date is not None else 0
        b.write(Int(flags))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        return b.getvalue()
