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


class SendAsPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendAsPeer`.

    Details:
        - Layer: ``227``
        - ID: ``B81C7034``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        premium_required (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer", "premium_required"]

    ID = 0xb81c7034
    QUALNAME = "types.SendAsPeer"

    def __init__(self, *, peer: "raw.base.Peer", premium_required: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.premium_required = premium_required  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendAsPeer":
        
        flags = Int.read(b)
        
        premium_required = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return SendAsPeer(peer=peer, premium_required=premium_required)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.premium_required else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
