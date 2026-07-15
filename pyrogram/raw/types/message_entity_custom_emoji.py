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


class MessageEntityCustomEmoji(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``227``
        - ID: ``C8CF05F8``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        document_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["offset", "length", "document_id"]

    ID = 0xc8cf05f8
    QUALNAME = "types.MessageEntityCustomEmoji"

    def __init__(self, *, offset: int, length: int, document_id: int) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityCustomEmoji":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        document_id = Long.read(b)
        
        return MessageEntityCustomEmoji(offset=offset, length=length, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(Long(self.document_id))
        
        return b.getvalue()
