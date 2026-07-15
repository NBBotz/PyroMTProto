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


class MessageActionTodoAppendTasks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``C7EDBC83``

    Parameters:
        list (List of :obj:`TodoItem <pyrogram.raw.base.TodoItem>`):
            N/A

    """

    __slots__: list[str] = ["list"]

    ID = 0xc7edbc83
    QUALNAME = "types.MessageActionTodoAppendTasks"

    def __init__(self, *, list: list["raw.base.TodoItem"]) -> None:
        self.list = list  # Vector<TodoItem>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTodoAppendTasks":
        # No flags
        
        list = TLObject.read(b)
        
        return MessageActionTodoAppendTasks(list=list)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.list))
        
        return b.getvalue()
