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


class SearchResultsPositions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SearchResultsPositions`.

    Details:
        - Layer: ``227``
        - ID: ``53B22BAF``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        positions (List of :obj:`SearchResultsPosition <pyrogram.raw.base.SearchResultsPosition>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSearchResultsPositions
    """

    __slots__: list[str] = ["count", "positions"]

    ID = 0x53b22baf
    QUALNAME = "types.messages.SearchResultsPositions"

    def __init__(self, *, count: int, positions: list["raw.base.SearchResultsPosition"]) -> None:
        self.count = count  # int
        self.positions = positions  # Vector<SearchResultsPosition>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsPositions":
        # No flags
        
        count = Int.read(b)
        
        positions = TLObject.read(b)
        
        return SearchResultsPositions(count=count, positions=positions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.positions))
        
        return b.getvalue()
