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


class RenameStickerSet(TLObject["raw.base.messages.StickerSet"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``124B1C00``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        title (``str``):
            N/A

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: list[str] = ["stickerset", "title"]

    ID = 0x124b1c00
    QUALNAME = "functions.stickers.RenameStickerSet"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", title: str) -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RenameStickerSet":
        # No flags
        
        stickerset = TLObject.read(b)
        
        title = String.read(b)
        
        return RenameStickerSet(stickerset=stickerset, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        b.write(String(self.title))
        
        return b.getvalue()
