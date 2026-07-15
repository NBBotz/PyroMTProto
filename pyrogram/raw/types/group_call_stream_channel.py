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


class GroupCallStreamChannel(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.GroupCallStreamChannel`.

    Details:
        - Layer: ``227``
        - ID: ``80EB48AF``

    Parameters:
        channel (``int`` ``32-bit``):
            N/A

        scale (``int`` ``32-bit``):
            N/A

        last_timestamp_ms (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["channel", "scale", "last_timestamp_ms"]

    ID = 0x80eb48af
    QUALNAME = "types.GroupCallStreamChannel"

    def __init__(self, *, channel: int, scale: int, last_timestamp_ms: int) -> None:
        self.channel = channel  # int
        self.scale = scale  # int
        self.last_timestamp_ms = last_timestamp_ms  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamChannel":
        # No flags
        
        channel = Int.read(b)
        
        scale = Int.read(b)
        
        last_timestamp_ms = Long.read(b)
        
        return GroupCallStreamChannel(channel=channel, scale=scale, last_timestamp_ms=last_timestamp_ms)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.channel))
        
        b.write(Int(self.scale))
        
        b.write(Long(self.last_timestamp_ms))
        
        return b.getvalue()
