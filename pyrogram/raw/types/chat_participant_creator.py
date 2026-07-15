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


class ChatParticipantCreator(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipant`.

    Details:
        - Layer: ``227``
        - ID: ``E1F867B8``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["user_id", "rank"]

    ID = 0xe1f867b8
    QUALNAME = "types.ChatParticipantCreator"

    def __init__(self, *, user_id: int, rank: Optional[str] = None) -> None:
        self.user_id = user_id  # long
        self.rank = rank  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantCreator":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        rank = String.read(b) if flags & (1 << 0) else None
        return ChatParticipantCreator(user_id=user_id, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()
