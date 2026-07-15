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


class CheckSearchPostsFlood(TLObject["raw.base.SearchPostsFlood"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``22567115``

    Parameters:
        query (``str``, *optional*):
            N/A

    Returns:
        :obj:`SearchPostsFlood <pyrogram.raw.base.SearchPostsFlood>`
    """

    __slots__: list[str] = ["query"]

    ID = 0x22567115
    QUALNAME = "functions.channels.CheckSearchPostsFlood"

    def __init__(self, *, query: Optional[str] = None) -> None:
        self.query = query  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckSearchPostsFlood":
        
        flags = Int.read(b)
        
        query = String.read(b) if flags & (1 << 0) else None
        return CheckSearchPostsFlood(query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.query is not None else 0
        b.write(Int(flags))
        
        if self.query is not None:
            b.write(String(self.query))
        
        return b.getvalue()
