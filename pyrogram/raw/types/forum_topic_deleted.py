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


class ForumTopicDeleted(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ForumTopic`.

    Details:
        - Layer: ``227``
        - ID: ``23F109B``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["id"]

    ID = 0x23f109b
    QUALNAME = "types.ForumTopicDeleted"

    def __init__(self, *, id: int) -> None:
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopicDeleted":
        # No flags
        
        id = Int.read(b)
        
        return ForumTopicDeleted(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        return b.getvalue()
