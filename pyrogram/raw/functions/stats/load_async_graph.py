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


class LoadAsyncGraph(TLObject["raw.base.StatsGraph"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``621D5FA0``

    Parameters:
        token (``str``):
            N/A

        x (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
    """

    __slots__: list[str] = ["token", "x"]

    ID = 0x621d5fa0
    QUALNAME = "functions.stats.LoadAsyncGraph"

    def __init__(self, *, token: str, x: Optional[int] = None) -> None:
        self.token = token  # string
        self.x = x  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoadAsyncGraph":
        
        flags = Int.read(b)
        
        token = String.read(b)
        
        x = Long.read(b) if flags & (1 << 0) else None
        return LoadAsyncGraph(token=token, x=x)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.x is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.token))
        
        if self.x is not None:
            b.write(Long(self.x))
        
        return b.getvalue()
