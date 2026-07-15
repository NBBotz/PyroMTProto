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


class TodoList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TodoList`.

    Details:
        - Layer: ``227``
        - ID: ``49B92A26``

    Parameters:
        title (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        list (List of :obj:`TodoItem <pyrogram.raw.base.TodoItem>`):
            N/A

        others_can_append (``bool``, *optional*):
            N/A

        others_can_complete (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["title", "list", "others_can_append", "others_can_complete"]

    ID = 0x49b92a26
    QUALNAME = "types.TodoList"

    def __init__(self, *, title: "raw.base.TextWithEntities", list: list["raw.base.TodoItem"], others_can_append: Optional[bool] = None, others_can_complete: Optional[bool] = None) -> None:
        self.title = title  # TextWithEntities
        self.list = list  # Vector<TodoItem>
        self.others_can_append = others_can_append  # flags.0?true
        self.others_can_complete = others_can_complete  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TodoList":
        
        flags = Int.read(b)
        
        others_can_append = True if flags & (1 << 0) else False
        others_can_complete = True if flags & (1 << 1) else False
        title = TLObject.read(b)
        
        list = TLObject.read(b)
        
        return TodoList(title=title, list=list, others_can_append=others_can_append, others_can_complete=others_can_complete)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.others_can_append else 0
        flags |= (1 << 1) if self.others_can_complete else 0
        b.write(Int(flags))
        
        b.write(self.title.write())
        
        b.write(Vector(self.list))
        
        return b.getvalue()
