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


class UpdatePinnedForumTopics(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``DEF143D0``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        order (List of ``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer", "order"]

    ID = 0xdef143d0
    QUALNAME = "types.UpdatePinnedForumTopics"

    def __init__(self, *, peer: "raw.base.Peer", order: Optional[list[int]] = None) -> None:
        self.peer = peer  # Peer
        self.order = order  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedForumTopics":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        order = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        return UpdatePinnedForumTopics(peer=peer, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.order is not None:
            b.write(Vector(self.order, Int))
        
        return b.getvalue()
