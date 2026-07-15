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


class TodoCompletion(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TodoCompletion`.

    Details:
        - Layer: ``227``
        - ID: ``221BB5E4``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        completed_by (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["id", "completed_by", "date"]

    ID = 0x221bb5e4
    QUALNAME = "types.TodoCompletion"

    def __init__(self, *, id: int, completed_by: "raw.base.Peer", date: int) -> None:
        self.id = id  # int
        self.completed_by = completed_by  # Peer
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TodoCompletion":
        # No flags
        
        id = Int.read(b)
        
        completed_by = TLObject.read(b)
        
        date = Int.read(b)
        
        return TodoCompletion(id=id, completed_by=completed_by, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(self.completed_by.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()
