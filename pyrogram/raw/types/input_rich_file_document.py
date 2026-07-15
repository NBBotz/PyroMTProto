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


class InputRichFileDocument(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputRichFile`.

    Details:
        - Layer: ``227``
        - ID: ``83281DBD``

    Parameters:
        id (``str``):
            N/A

        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

    """

    __slots__: list[str] = ["id", "document"]

    ID = 0x83281dbd
    QUALNAME = "types.InputRichFileDocument"

    def __init__(self, *, id: str, document: "raw.base.InputDocument") -> None:
        self.id = id  # string
        self.document = document  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputRichFileDocument":
        # No flags
        
        id = String.read(b)
        
        document = TLObject.read(b)
        
        return InputRichFileDocument(id=id, document=document)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(self.document.write())
        
        return b.getvalue()
