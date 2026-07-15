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


class BusinessIntro(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BusinessIntro`.

    Details:
        - Layer: ``227``
        - ID: ``5A0A066D``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        sticker (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["title", "description", "sticker"]

    ID = 0x5a0a066d
    QUALNAME = "types.BusinessIntro"

    def __init__(self, *, title: str, description: str, sticker: "raw.base.Document" = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.sticker = sticker  # flags.0?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessIntro":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        sticker = TLObject.read(b) if flags & (1 << 0) else None
        
        return BusinessIntro(title=title, description=description, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sticker is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.sticker is not None:
            b.write(self.sticker.write())
        
        return b.getvalue()
