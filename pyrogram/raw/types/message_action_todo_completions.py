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


class MessageActionTodoCompletions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``CC7C5C89``

    Parameters:
        completed (List of ``int`` ``32-bit``):
            N/A

        incompleted (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["completed", "incompleted"]

    ID = 0xcc7c5c89
    QUALNAME = "types.MessageActionTodoCompletions"

    def __init__(self, *, completed: list[int], incompleted: list[int]) -> None:
        self.completed = completed  # Vector<int>
        self.incompleted = incompleted  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTodoCompletions":
        # No flags
        
        completed = TLObject.read(b, Int)
        
        incompleted = TLObject.read(b, Int)
        
        return MessageActionTodoCompletions(completed=completed, incompleted=incompleted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.completed, Int))
        
        b.write(Vector(self.incompleted, Int))
        
        return b.getvalue()
