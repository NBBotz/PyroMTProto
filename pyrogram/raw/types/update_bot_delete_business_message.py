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


class UpdateBotDeleteBusinessMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``A02A982E``

    Parameters:
        connection_id (``str``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        messages (List of ``int`` ``32-bit``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["connection_id", "peer", "messages", "qts"]

    ID = 0xa02a982e
    QUALNAME = "types.UpdateBotDeleteBusinessMessage"

    def __init__(self, *, connection_id: str, peer: "raw.base.Peer", messages: list[int], qts: int) -> None:
        self.connection_id = connection_id  # string
        self.peer = peer  # Peer
        self.messages = messages  # Vector<int>
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotDeleteBusinessMessage":
        # No flags
        
        connection_id = String.read(b)
        
        peer = TLObject.read(b)
        
        messages = TLObject.read(b, Int)
        
        qts = Int.read(b)
        
        return UpdateBotDeleteBusinessMessage(connection_id=connection_id, peer=peer, messages=messages, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.connection_id))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.messages, Int))
        
        b.write(Int(self.qts))
        
        return b.getvalue()
