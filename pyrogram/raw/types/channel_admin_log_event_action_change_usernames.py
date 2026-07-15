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


class ChannelAdminLogEventActionChangeUsernames(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``227``
        - ID: ``F04FB3A9``

    Parameters:
        prev_value (List of ``str``):
            N/A

        new_value (List of ``str``):
            N/A

    """

    __slots__: list[str] = ["prev_value", "new_value"]

    ID = 0xf04fb3a9
    QUALNAME = "types.ChannelAdminLogEventActionChangeUsernames"

    def __init__(self, *, prev_value: list[str], new_value: list[str]) -> None:
        self.prev_value = prev_value  # Vector<string>
        self.new_value = new_value  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeUsernames":
        # No flags
        
        prev_value = TLObject.read(b, String)
        
        new_value = TLObject.read(b, String)
        
        return ChannelAdminLogEventActionChangeUsernames(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.prev_value, String))
        
        b.write(Vector(self.new_value, String))
        
        return b.getvalue()
