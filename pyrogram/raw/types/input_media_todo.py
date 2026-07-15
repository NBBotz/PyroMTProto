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


class InputMediaTodo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``227``
        - ID: ``9FC55FDE``

    Parameters:
        todo (:obj:`TodoList <pyrogram.raw.base.TodoList>`):
            N/A

    """

    __slots__: list[str] = ["todo"]

    ID = 0x9fc55fde
    QUALNAME = "types.InputMediaTodo"

    def __init__(self, *, todo: "raw.base.TodoList") -> None:
        self.todo = todo  # TodoList

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaTodo":
        # No flags
        
        todo = TLObject.read(b)
        
        return InputMediaTodo(todo=todo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.todo.write())
        
        return b.getvalue()
