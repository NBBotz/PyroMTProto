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


class TextCustomEmoji(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``227``
        - ID: ``A26156C0``

    Parameters:
        document_id (``int`` ``64-bit``):
            N/A

        alt (``str``):
            N/A

    """

    __slots__: list[str] = ["document_id", "alt"]

    ID = 0xa26156c0
    QUALNAME = "types.TextCustomEmoji"

    def __init__(self, *, document_id: int, alt: str) -> None:
        self.document_id = document_id  # long
        self.alt = alt  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextCustomEmoji":
        # No flags
        
        document_id = Long.read(b)
        
        alt = String.read(b)
        
        return TextCustomEmoji(document_id=document_id, alt=alt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        b.write(String(self.alt))
        
        return b.getvalue()
