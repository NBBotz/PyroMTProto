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


class ChannelAdminLogEventActionParticipantEditRank(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``227``
        - ID: ``5806B4EC``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        prev_rank (``str``):
            N/A

        new_rank (``str``):
            N/A

    """

    __slots__: list[str] = ["user_id", "prev_rank", "new_rank"]

    ID = 0x5806b4ec
    QUALNAME = "types.ChannelAdminLogEventActionParticipantEditRank"

    def __init__(self, *, user_id: int, prev_rank: str, new_rank: str) -> None:
        self.user_id = user_id  # long
        self.prev_rank = prev_rank  # string
        self.new_rank = new_rank  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantEditRank":
        # No flags
        
        user_id = Long.read(b)
        
        prev_rank = String.read(b)
        
        new_rank = String.read(b)
        
        return ChannelAdminLogEventActionParticipantEditRank(user_id=user_id, prev_rank=prev_rank, new_rank=new_rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(String(self.prev_rank))
        
        b.write(String(self.new_rank))
        
        return b.getvalue()
