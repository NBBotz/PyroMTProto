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


class MessageActionNoForwardsRequest(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``3E2793BA``

    Parameters:
        prev_value (``bool``):
            N/A

        new_value (``bool``):
            N/A

        expired (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["prev_value", "new_value", "expired"]

    ID = 0x3e2793ba
    QUALNAME = "types.MessageActionNoForwardsRequest"

    def __init__(self, *, prev_value: bool, new_value: bool, expired: Optional[bool] = None) -> None:
        self.prev_value = prev_value  # Bool
        self.new_value = new_value  # Bool
        self.expired = expired  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionNoForwardsRequest":
        
        flags = Int.read(b)
        
        expired = True if flags & (1 << 0) else False
        prev_value = Bool.read(b)
        
        new_value = Bool.read(b)
        
        return MessageActionNoForwardsRequest(prev_value=prev_value, new_value=new_value, expired=expired)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.expired else 0
        b.write(Int(flags))
        
        b.write(Bool(self.prev_value))
        
        b.write(Bool(self.new_value))
        
        return b.getvalue()
