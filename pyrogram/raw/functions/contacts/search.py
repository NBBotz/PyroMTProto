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


class Search(TLObject["raw.base.contacts.Found"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``5F58D0F``

    Parameters:
        q (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        broadcasts (``bool``, *optional*):
            N/A

        bots (``bool``, *optional*):
            N/A

    Returns:
        :obj:`contacts.Found <pyrogram.raw.base.contacts.Found>`
    """

    __slots__: list[str] = ["q", "limit", "broadcasts", "bots"]

    ID = 0x5f58d0f
    QUALNAME = "functions.contacts.Search"

    def __init__(self, *, q: str, limit: int, broadcasts: Optional[bool] = None, bots: Optional[bool] = None) -> None:
        self.q = q  # string
        self.limit = limit  # int
        self.broadcasts = broadcasts  # flags.0?true
        self.bots = bots  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Search":
        
        flags = Int.read(b)
        
        broadcasts = True if flags & (1 << 0) else False
        bots = True if flags & (1 << 1) else False
        q = String.read(b)
        
        limit = Int.read(b)
        
        return Search(q=q, limit=limit, broadcasts=broadcasts, bots=bots)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcasts else 0
        flags |= (1 << 1) if self.bots else 0
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
