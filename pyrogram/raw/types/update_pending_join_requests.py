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


class UpdatePendingJoinRequests(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``7063C3DB``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        requests_pending (``int`` ``32-bit``):
            N/A

        recent_requesters (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["peer", "requests_pending", "recent_requesters"]

    ID = 0x7063c3db
    QUALNAME = "types.UpdatePendingJoinRequests"

    def __init__(self, *, peer: "raw.base.Peer", requests_pending: int, recent_requesters: list[int]) -> None:
        self.peer = peer  # Peer
        self.requests_pending = requests_pending  # int
        self.recent_requesters = recent_requesters  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePendingJoinRequests":
        # No flags
        
        peer = TLObject.read(b)
        
        requests_pending = Int.read(b)
        
        recent_requesters = TLObject.read(b, Long)
        
        return UpdatePendingJoinRequests(peer=peer, requests_pending=requests_pending, recent_requesters=recent_requesters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.requests_pending))
        
        b.write(Vector(self.recent_requesters, Long))
        
        return b.getvalue()
