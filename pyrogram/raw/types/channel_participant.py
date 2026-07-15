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


class ChannelParticipant(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``227``
        - ID: ``1BD54456``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        subscription_until_date (``int`` ``32-bit``, *optional*):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["user_id", "date", "subscription_until_date", "rank"]

    ID = 0x1bd54456
    QUALNAME = "types.ChannelParticipant"

    def __init__(self, *, user_id: int, date: int, subscription_until_date: Optional[int] = None, rank: Optional[str] = None) -> None:
        self.user_id = user_id  # long
        self.date = date  # int
        self.subscription_until_date = subscription_until_date  # flags.0?int
        self.rank = rank  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipant":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        date = Int.read(b)
        
        subscription_until_date = Int.read(b) if flags & (1 << 0) else None
        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipant(user_id=user_id, date=date, subscription_until_date=subscription_until_date, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.subscription_until_date is not None else 0
        flags |= (1 << 2) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.date))
        
        if self.subscription_until_date is not None:
            b.write(Int(self.subscription_until_date))
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()
