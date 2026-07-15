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


class Albums(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.Albums`.

    Details:
        - Layer: ``227``
        - ID: ``C3987A3A``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        albums (List of :obj:`StoryAlbum <pyrogram.raw.base.StoryAlbum>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetAlbums
    """

    __slots__: list[str] = ["hash", "albums"]

    ID = 0xc3987a3a
    QUALNAME = "types.stories.Albums"

    def __init__(self, *, hash: int, albums: list["raw.base.StoryAlbum"]) -> None:
        self.hash = hash  # long
        self.albums = albums  # Vector<StoryAlbum>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Albums":
        # No flags
        
        hash = Long.read(b)
        
        albums = TLObject.read(b)
        
        return Albums(hash=hash, albums=albums)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.albums))
        
        return b.getvalue()
