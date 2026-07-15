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


class StarGiftAuctionStateFinished(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAuctionState`.

    Details:
        - Layer: ``227``
        - ID: ``972DABBF``

    Parameters:
        start_date (``int`` ``32-bit``):
            N/A

        end_date (``int`` ``32-bit``):
            N/A

        average_price (``int`` ``64-bit``):
            N/A

        listed_count (``int`` ``32-bit``, *optional*):
            N/A

        fragment_listed_count (``int`` ``32-bit``, *optional*):
            N/A

        fragment_listed_url (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["start_date", "end_date", "average_price", "listed_count", "fragment_listed_count", "fragment_listed_url"]

    ID = 0x972dabbf
    QUALNAME = "types.StarGiftAuctionStateFinished"

    def __init__(self, *, start_date: int, end_date: int, average_price: int, listed_count: Optional[int] = None, fragment_listed_count: Optional[int] = None, fragment_listed_url: Optional[str] = None) -> None:
        self.start_date = start_date  # int
        self.end_date = end_date  # int
        self.average_price = average_price  # long
        self.listed_count = listed_count  # flags.0?int
        self.fragment_listed_count = fragment_listed_count  # flags.1?int
        self.fragment_listed_url = fragment_listed_url  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionStateFinished":
        
        flags = Int.read(b)
        
        start_date = Int.read(b)
        
        end_date = Int.read(b)
        
        average_price = Long.read(b)
        
        listed_count = Int.read(b) if flags & (1 << 0) else None
        fragment_listed_count = Int.read(b) if flags & (1 << 1) else None
        fragment_listed_url = String.read(b) if flags & (1 << 1) else None
        return StarGiftAuctionStateFinished(start_date=start_date, end_date=end_date, average_price=average_price, listed_count=listed_count, fragment_listed_count=fragment_listed_count, fragment_listed_url=fragment_listed_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.listed_count is not None else 0
        flags |= (1 << 1) if self.fragment_listed_count is not None else 0
        flags |= (1 << 1) if self.fragment_listed_url is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.start_date))
        
        b.write(Int(self.end_date))
        
        b.write(Long(self.average_price))
        
        if self.listed_count is not None:
            b.write(Int(self.listed_count))
        
        if self.fragment_listed_count is not None:
            b.write(Int(self.fragment_listed_count))
        
        if self.fragment_listed_url is not None:
            b.write(String(self.fragment_listed_url))
        
        return b.getvalue()
