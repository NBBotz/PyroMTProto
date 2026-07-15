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


class SavedGifs(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedGifs`.

    Details:
        - Layer: ``227``
        - ID: ``84A02A0D``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        gifs (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedGifs
    """

    __slots__: list[str] = ["hash", "gifs"]

    ID = 0x84a02a0d
    QUALNAME = "types.messages.SavedGifs"

    def __init__(self, *, hash: int, gifs: list["raw.base.Document"]) -> None:
        self.hash = hash  # long
        self.gifs = gifs  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedGifs":
        # No flags
        
        hash = Long.read(b)
        
        gifs = TLObject.read(b)
        
        return SavedGifs(hash=hash, gifs=gifs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.gifs))
        
        return b.getvalue()
