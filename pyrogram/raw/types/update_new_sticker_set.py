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


class UpdateNewStickerSet(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``688A30AA``

    Parameters:
        stickerset (:obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`):
            N/A

    """

    __slots__: list[str] = ["stickerset"]

    ID = 0x688a30aa
    QUALNAME = "types.UpdateNewStickerSet"

    def __init__(self, *, stickerset: "raw.base.messages.StickerSet") -> None:
        self.stickerset = stickerset  # messages.StickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewStickerSet":
        # No flags
        
        stickerset = TLObject.read(b)
        
        return UpdateNewStickerSet(stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        return b.getvalue()
