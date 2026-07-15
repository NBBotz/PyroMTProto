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


class MessageEntityBlockquote(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``227``
        - ID: ``F1CCAAAC``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        collapsed (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["offset", "length", "collapsed"]

    ID = 0xf1ccaaac
    QUALNAME = "types.MessageEntityBlockquote"

    def __init__(self, *, offset: int, length: int, collapsed: Optional[bool] = None) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.collapsed = collapsed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityBlockquote":
        
        flags = Int.read(b)
        
        collapsed = True if flags & (1 << 0) else False
        offset = Int.read(b)
        
        length = Int.read(b)
        
        return MessageEntityBlockquote(offset=offset, length=length, collapsed=collapsed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.collapsed else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        return b.getvalue()
