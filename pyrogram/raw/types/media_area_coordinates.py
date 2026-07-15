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


class MediaAreaCoordinates(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaAreaCoordinates`.

    Details:
        - Layer: ``227``
        - ID: ``CFC9E002``

    Parameters:
        x (``float`` ``64-bit``):
            N/A

        y (``float`` ``64-bit``):
            N/A

        w (``float`` ``64-bit``):
            N/A

        h (``float`` ``64-bit``):
            N/A

        rotation (``float`` ``64-bit``):
            N/A

        radius (``float`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["x", "y", "w", "h", "rotation", "radius"]

    ID = 0xcfc9e002
    QUALNAME = "types.MediaAreaCoordinates"

    def __init__(self, *, x: float, y: float, w: float, h: float, rotation: float, radius: Optional[float] = None) -> None:
        self.x = x  # double
        self.y = y  # double
        self.w = w  # double
        self.h = h  # double
        self.rotation = rotation  # double
        self.radius = radius  # flags.0?double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaCoordinates":
        
        flags = Int.read(b)
        
        x = Double.read(b)
        
        y = Double.read(b)
        
        w = Double.read(b)
        
        h = Double.read(b)
        
        rotation = Double.read(b)
        
        radius = Double.read(b) if flags & (1 << 0) else None
        return MediaAreaCoordinates(x=x, y=y, w=w, h=h, rotation=rotation, radius=radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.radius is not None else 0
        b.write(Int(flags))
        
        b.write(Double(self.x))
        
        b.write(Double(self.y))
        
        b.write(Double(self.w))
        
        b.write(Double(self.h))
        
        b.write(Double(self.rotation))
        
        if self.radius is not None:
            b.write(Double(self.radius))
        
        return b.getvalue()
