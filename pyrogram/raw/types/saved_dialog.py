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


class SavedDialog(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SavedDialog`.

    Details:
        - Layer: ``227``
        - ID: ``BD87CB6C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        top_message (``int`` ``32-bit``):
            N/A

        pinned (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer", "top_message", "pinned"]

    ID = 0xbd87cb6c
    QUALNAME = "types.SavedDialog"

    def __init__(self, *, peer: "raw.base.Peer", top_message: int, pinned: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.pinned = pinned  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialog":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        top_message = Int.read(b)
        
        return SavedDialog(peer=peer, top_message=top_message, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        return b.getvalue()
