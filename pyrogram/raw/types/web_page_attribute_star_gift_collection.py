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


class WebPageAttributeStarGiftCollection(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``227``
        - ID: ``31CAD303``

    Parameters:
        icons (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    """

    __slots__: list[str] = ["icons"]

    ID = 0x31cad303
    QUALNAME = "types.WebPageAttributeStarGiftCollection"

    def __init__(self, *, icons: list["raw.base.Document"]) -> None:
        self.icons = icons  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStarGiftCollection":
        # No flags
        
        icons = TLObject.read(b)
        
        return WebPageAttributeStarGiftCollection(icons=icons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.icons))
        
        return b.getvalue()
