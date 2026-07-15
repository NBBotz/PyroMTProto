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


class MessageActionRequestedPeerSentMe(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``93B31848``

    Parameters:
        button_id (``int`` ``32-bit``):
            N/A

        peers (List of :obj:`RequestedPeer <pyrogram.raw.base.RequestedPeer>`):
            N/A

    """

    __slots__: list[str] = ["button_id", "peers"]

    ID = 0x93b31848
    QUALNAME = "types.MessageActionRequestedPeerSentMe"

    def __init__(self, *, button_id: int, peers: list["raw.base.RequestedPeer"]) -> None:
        self.button_id = button_id  # int
        self.peers = peers  # Vector<RequestedPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionRequestedPeerSentMe":
        # No flags
        
        button_id = Int.read(b)
        
        peers = TLObject.read(b)
        
        return MessageActionRequestedPeerSentMe(button_id=button_id, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.button_id))
        
        b.write(Vector(self.peers))
        
        return b.getvalue()
