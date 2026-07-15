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


class MessageEntityDiffReplace(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``227``
        - ID: ``C6C1E5A7``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        old_text (``str``):
            N/A

    """

    __slots__: list[str] = ["offset", "length", "old_text"]

    ID = 0xc6c1e5a7
    QUALNAME = "types.MessageEntityDiffReplace"

    def __init__(self, *, offset: int, length: int, old_text: str) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.old_text = old_text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityDiffReplace":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        old_text = String.read(b)
        
        return MessageEntityDiffReplace(offset=offset, length=length, old_text=old_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(String(self.old_text))
        
        return b.getvalue()
