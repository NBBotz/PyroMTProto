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


class TimezonesList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.TimezonesList`.

    Details:
        - Layer: ``227``
        - ID: ``7B74ED71``

    Parameters:
        timezones (List of :obj:`Timezone <pyrogram.raw.base.Timezone>`):
            N/A

        hash (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTimezonesList
    """

    __slots__: list[str] = ["timezones", "hash"]

    ID = 0x7b74ed71
    QUALNAME = "types.help.TimezonesList"

    def __init__(self, *, timezones: list["raw.base.Timezone"], hash: int) -> None:
        self.timezones = timezones  # Vector<Timezone>
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TimezonesList":
        # No flags
        
        timezones = TLObject.read(b)
        
        hash = Int.read(b)
        
        return TimezonesList(timezones=timezones, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.timezones))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
