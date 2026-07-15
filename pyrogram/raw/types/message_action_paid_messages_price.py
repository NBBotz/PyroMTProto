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


class MessageActionPaidMessagesPrice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``84B88578``

    Parameters:
        stars (``int`` ``64-bit``):
            N/A

        broadcast_messages_allowed (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["stars", "broadcast_messages_allowed"]

    ID = 0x84b88578
    QUALNAME = "types.MessageActionPaidMessagesPrice"

    def __init__(self, *, stars: int, broadcast_messages_allowed: Optional[bool] = None) -> None:
        self.stars = stars  # long
        self.broadcast_messages_allowed = broadcast_messages_allowed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaidMessagesPrice":
        
        flags = Int.read(b)
        
        broadcast_messages_allowed = True if flags & (1 << 0) else False
        stars = Long.read(b)
        
        return MessageActionPaidMessagesPrice(stars=stars, broadcast_messages_allowed=broadcast_messages_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcast_messages_allowed else 0
        b.write(Int(flags))
        
        b.write(Long(self.stars))
        
        return b.getvalue()
