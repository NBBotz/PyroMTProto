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


class BotCancelStarsSubscription(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``6DFA0622``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        charge_id (``str``):
            N/A

        restore (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["user_id", "charge_id", "restore"]

    ID = 0x6dfa0622
    QUALNAME = "functions.payments.BotCancelStarsSubscription"

    def __init__(self, *, user_id: "raw.base.InputUser", charge_id: str, restore: Optional[bool] = None) -> None:
        self.user_id = user_id  # InputUser
        self.charge_id = charge_id  # string
        self.restore = restore  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCancelStarsSubscription":
        
        flags = Int.read(b)
        
        restore = True if flags & (1 << 0) else False
        user_id = TLObject.read(b)
        
        charge_id = String.read(b)
        
        return BotCancelStarsSubscription(user_id=user_id, charge_id=charge_id, restore=restore)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.restore else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(String(self.charge_id))
        
        return b.getvalue()
