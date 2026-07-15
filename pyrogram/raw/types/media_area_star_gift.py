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


class MediaAreaStarGift(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``227``
        - ID: ``5787686D``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        slug (``str``):
            N/A

    """

    __slots__: list[str] = ["coordinates", "slug"]

    ID = 0x5787686d
    QUALNAME = "types.MediaAreaStarGift"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", slug: str) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaStarGift":
        # No flags
        
        coordinates = TLObject.read(b)
        
        slug = String.read(b)
        
        return MediaAreaStarGift(coordinates=coordinates, slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(String(self.slug))
        
        return b.getvalue()
