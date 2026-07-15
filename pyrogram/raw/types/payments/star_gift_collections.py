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


class StarGiftCollections(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftCollections`.

    Details:
        - Layer: ``227``
        - ID: ``8A2932F3``

    Parameters:
        collections (List of :obj:`StarGiftCollection <pyrogram.raw.base.StarGiftCollection>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftCollections
    """

    __slots__: list[str] = ["collections"]

    ID = 0x8a2932f3
    QUALNAME = "types.payments.StarGiftCollections"

    def __init__(self, *, collections: list["raw.base.StarGiftCollection"]) -> None:
        self.collections = collections  # Vector<StarGiftCollection>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftCollections":
        # No flags
        
        collections = TLObject.read(b)
        
        return StarGiftCollections(collections=collections)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.collections))
        
        return b.getvalue()
