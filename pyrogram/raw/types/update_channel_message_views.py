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


class UpdateChannelMessageViews(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``F226AC08``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        id (``int`` ``32-bit``):
            N/A

        views (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["channel_id", "id", "views"]

    ID = 0xf226ac08
    QUALNAME = "types.UpdateChannelMessageViews"

    def __init__(self, *, channel_id: int, id: int, views: int) -> None:
        self.channel_id = channel_id  # long
        self.id = id  # int
        self.views = views  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelMessageViews":
        # No flags
        
        channel_id = Long.read(b)
        
        id = Int.read(b)
        
        views = Int.read(b)
        
        return UpdateChannelMessageViews(channel_id=channel_id, id=id, views=views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.id))
        
        b.write(Int(self.views))
        
        return b.getvalue()
