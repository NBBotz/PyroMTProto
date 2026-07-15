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


class StickerPack(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StickerPack`.

    Details:
        - Layer: ``227``
        - ID: ``12B299D4``

    Parameters:
        emoticon (``str``):
            N/A

        documents (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["emoticon", "documents"]

    ID = 0x12b299d4
    QUALNAME = "types.StickerPack"

    def __init__(self, *, emoticon: str, documents: list[int]) -> None:
        self.emoticon = emoticon  # string
        self.documents = documents  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerPack":
        # No flags
        
        emoticon = String.read(b)
        
        documents = TLObject.read(b, Long)
        
        return StickerPack(emoticon=emoticon, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.emoticon))
        
        b.write(Vector(self.documents, Long))
        
        return b.getvalue()
