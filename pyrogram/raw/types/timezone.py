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


class Timezone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Timezone`.

    Details:
        - Layer: ``227``
        - ID: ``FF9289F5``

    Parameters:
        id (``str``):
            N/A

        name (``str``):
            N/A

        utc_offset (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["id", "name", "utc_offset"]

    ID = 0xff9289f5
    QUALNAME = "types.Timezone"

    def __init__(self, *, id: str, name: str, utc_offset: int) -> None:
        self.id = id  # string
        self.name = name  # string
        self.utc_offset = utc_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Timezone":
        # No flags
        
        id = String.read(b)
        
        name = String.read(b)
        
        utc_offset = Int.read(b)
        
        return Timezone(id=id, name=name, utc_offset=utc_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(String(self.name))
        
        b.write(Int(self.utc_offset))
        
        return b.getvalue()
