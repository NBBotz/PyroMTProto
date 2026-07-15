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


class UpdateBotChatBoost(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``904DD49C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        boost (:obj:`Boost <pyrogram.raw.base.Boost>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["peer", "boost", "qts"]

    ID = 0x904dd49c
    QUALNAME = "types.UpdateBotChatBoost"

    def __init__(self, *, peer: "raw.base.Peer", boost: "raw.base.Boost", qts: int) -> None:
        self.peer = peer  # Peer
        self.boost = boost  # Boost
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotChatBoost":
        # No flags
        
        peer = TLObject.read(b)
        
        boost = TLObject.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotChatBoost(peer=peer, boost=boost, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.boost.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
