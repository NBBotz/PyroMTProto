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


class GetCustomEmojiDocuments(TLObject["List[raw.base.Document]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``D9AB0F54``

    Parameters:
        document_id (List of ``int`` ``64-bit``):
            N/A

    Returns:
        List of :obj:`Document <pyrogram.raw.base.Document>`
    """

    __slots__: list[str] = ["document_id"]

    ID = 0xd9ab0f54
    QUALNAME = "functions.messages.GetCustomEmojiDocuments"

    def __init__(self, *, document_id: list[int]) -> None:
        self.document_id = document_id  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCustomEmojiDocuments":
        # No flags
        
        document_id = TLObject.read(b, Long)
        
        return GetCustomEmojiDocuments(document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.document_id, Long))
        
        return b.getvalue()
