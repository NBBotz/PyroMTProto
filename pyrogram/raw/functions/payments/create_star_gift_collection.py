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


class CreateStarGiftCollection(TLObject["raw.base.StarGiftCollection"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``1F4A0E87``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        title (``str``):
            N/A

        stargift (List of :obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

    Returns:
        :obj:`StarGiftCollection <pyrogram.raw.base.StarGiftCollection>`
    """

    __slots__: list[str] = ["peer", "title", "stargift"]

    ID = 0x1f4a0e87
    QUALNAME = "functions.payments.CreateStarGiftCollection"

    def __init__(self, *, peer: "raw.base.InputPeer", title: str, stargift: list["raw.base.InputSavedStarGift"]) -> None:
        self.peer = peer  # InputPeer
        self.title = title  # string
        self.stargift = stargift  # Vector<InputSavedStarGift>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateStarGiftCollection":
        # No flags
        
        peer = TLObject.read(b)
        
        title = String.read(b)
        
        stargift = TLObject.read(b)
        
        return CreateStarGiftCollection(peer=peer, title=title, stargift=stargift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(String(self.title))
        
        b.write(Vector(self.stargift))
        
        return b.getvalue()
