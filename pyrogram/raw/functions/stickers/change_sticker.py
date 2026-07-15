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


class ChangeSticker(TLObject["raw.base.messages.StickerSet"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``F5537EBC``

    Parameters:
        sticker (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        emoji (``str``, *optional*):
            N/A

        mask_coords (:obj:`MaskCoords <pyrogram.raw.base.MaskCoords>`, *optional*):
            N/A

        keywords (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: list[str] = ["sticker", "emoji", "mask_coords", "keywords"]

    ID = 0xf5537ebc
    QUALNAME = "functions.stickers.ChangeSticker"

    def __init__(self, *, sticker: "raw.base.InputDocument", emoji: Optional[str] = None, mask_coords: "raw.base.MaskCoords" = None, keywords: Optional[str] = None) -> None:
        self.sticker = sticker  # InputDocument
        self.emoji = emoji  # flags.0?string
        self.mask_coords = mask_coords  # flags.1?MaskCoords
        self.keywords = keywords  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeSticker":
        
        flags = Int.read(b)
        
        sticker = TLObject.read(b)
        
        emoji = String.read(b) if flags & (1 << 0) else None
        mask_coords = TLObject.read(b) if flags & (1 << 1) else None
        
        keywords = String.read(b) if flags & (1 << 2) else None
        return ChangeSticker(sticker=sticker, emoji=emoji, mask_coords=mask_coords, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.emoji is not None else 0
        flags |= (1 << 1) if self.mask_coords is not None else 0
        flags |= (1 << 2) if self.keywords is not None else 0
        b.write(Int(flags))
        
        b.write(self.sticker.write())
        
        if self.emoji is not None:
            b.write(String(self.emoji))
        
        if self.mask_coords is not None:
            b.write(self.mask_coords.write())
        
        if self.keywords is not None:
            b.write(String(self.keywords))
        
        return b.getvalue()
