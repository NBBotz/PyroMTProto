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


class PhotosSlice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.photos.Photos`.

    Details:
        - Layer: ``227``
        - ID: ``15051F54``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        photos (List of :obj:`Photo <pyrogram.raw.base.Photo>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            photos.GetUserPhotos
    """

    __slots__: list[str] = ["count", "photos", "users"]

    ID = 0x15051f54
    QUALNAME = "types.photos.PhotosSlice"

    def __init__(self, *, count: int, photos: list["raw.base.Photo"], users: list["raw.base.User"]) -> None:
        self.count = count  # int
        self.photos = photos  # Vector<Photo>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotosSlice":
        # No flags
        
        count = Int.read(b)
        
        photos = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PhotosSlice(count=count, photos=photos, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
