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


class CountriesList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.CountriesList`.

    Details:
        - Layer: ``227``
        - ID: ``87D0759E``

    Parameters:
        countries (List of :obj:`help.Country <pyrogram.raw.base.help.Country>`):
            N/A

        hash (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetCountriesList
    """

    __slots__: list[str] = ["countries", "hash"]

    ID = 0x87d0759e
    QUALNAME = "types.help.CountriesList"

    def __init__(self, *, countries: list["raw.base.help.Country"], hash: int) -> None:
        self.countries = countries  # Vector<help.Country>
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CountriesList":
        # No flags
        
        countries = TLObject.read(b)
        
        hash = Int.read(b)
        
        return CountriesList(countries=countries, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.countries))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
