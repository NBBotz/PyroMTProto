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


class ChannelAdminLogEventActionChangeWallpaper(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``227``
        - ID: ``31BB5D52``

    Parameters:
        prev_value (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`):
            N/A

        new_value (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`):
            N/A

    """

    __slots__: list[str] = ["prev_value", "new_value"]

    ID = 0x31bb5d52
    QUALNAME = "types.ChannelAdminLogEventActionChangeWallpaper"

    def __init__(self, *, prev_value: "raw.base.WallPaper", new_value: "raw.base.WallPaper") -> None:
        self.prev_value = prev_value  # WallPaper
        self.new_value = new_value  # WallPaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeWallpaper":
        # No flags
        
        prev_value = TLObject.read(b)
        
        new_value = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangeWallpaper(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()
