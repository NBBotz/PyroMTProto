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


class WebPageAttributeStickerSet(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``227``
        - ID: ``50CC03D3``

    Parameters:
        stickers (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        emojis (``bool``, *optional*):
            N/A

        text_color (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["stickers", "emojis", "text_color"]

    ID = 0x50cc03d3
    QUALNAME = "types.WebPageAttributeStickerSet"

    def __init__(self, *, stickers: list["raw.base.Document"], emojis: Optional[bool] = None, text_color: Optional[bool] = None) -> None:
        self.stickers = stickers  # Vector<Document>
        self.emojis = emojis  # flags.0?true
        self.text_color = text_color  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStickerSet":
        
        flags = Int.read(b)
        
        emojis = True if flags & (1 << 0) else False
        text_color = True if flags & (1 << 1) else False
        stickers = TLObject.read(b)
        
        return WebPageAttributeStickerSet(stickers=stickers, emojis=emojis, text_color=text_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.emojis else 0
        flags |= (1 << 1) if self.text_color else 0
        b.write(Int(flags))
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()
