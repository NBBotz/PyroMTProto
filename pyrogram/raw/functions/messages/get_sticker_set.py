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


class GetStickerSet(TLObject["raw.base.messages.StickerSet"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``C8A0EC74``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: list[str] = ["stickerset", "hash"]

    ID = 0xc8a0ec74
    QUALNAME = "functions.messages.GetStickerSet"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", hash: int) -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStickerSet":
        # No flags
        
        stickerset = TLObject.read(b)
        
        hash = Int.read(b)
        
        return GetStickerSet(stickerset=stickerset, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        b.write(Int(self.hash))
        
        return b.getvalue()
