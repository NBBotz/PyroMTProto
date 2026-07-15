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


class WebPageAttributeTheme(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``227``
        - ID: ``54B56617``

    Parameters:
        documents (List of :obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        settings (:obj:`ThemeSettings <pyrogram.raw.base.ThemeSettings>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["documents", "settings"]

    ID = 0x54b56617
    QUALNAME = "types.WebPageAttributeTheme"

    def __init__(self, *, documents: Optional[list["raw.base.Document"]] = None, settings: "raw.base.ThemeSettings" = None) -> None:
        self.documents = documents  # flags.0?Vector<Document>
        self.settings = settings  # flags.1?ThemeSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeTheme":
        
        flags = Int.read(b)
        
        documents = TLObject.read(b) if flags & (1 << 0) else []
        
        settings = TLObject.read(b) if flags & (1 << 1) else None
        
        return WebPageAttributeTheme(documents=documents, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.documents else 0
        flags |= (1 << 1) if self.settings is not None else 0
        b.write(Int(flags))
        
        if self.documents is not None:
            b.write(Vector(self.documents))
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        return b.getvalue()
