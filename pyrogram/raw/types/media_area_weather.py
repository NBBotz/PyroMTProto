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


class MediaAreaWeather(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``227``
        - ID: ``49A6549C``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        emoji (``str``):
            N/A

        temperature_c (``float`` ``64-bit``):
            N/A

        color (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["coordinates", "emoji", "temperature_c", "color"]

    ID = 0x49a6549c
    QUALNAME = "types.MediaAreaWeather"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", emoji: str, temperature_c: float, color: int) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.emoji = emoji  # string
        self.temperature_c = temperature_c  # double
        self.color = color  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaWeather":
        # No flags
        
        coordinates = TLObject.read(b)
        
        emoji = String.read(b)
        
        temperature_c = Double.read(b)
        
        color = Int.read(b)
        
        return MediaAreaWeather(coordinates=coordinates, emoji=emoji, temperature_c=temperature_c, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(String(self.emoji))
        
        b.write(Double(self.temperature_c))
        
        b.write(Int(self.color))
        
        return b.getvalue()
