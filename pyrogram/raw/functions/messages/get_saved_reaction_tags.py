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


class GetSavedReactionTags(TLObject["raw.base.messages.SavedReactionTags"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``3637E05B``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`messages.SavedReactionTags <pyrogram.raw.base.messages.SavedReactionTags>`
    """

    __slots__: list[str] = ["hash", "peer"]

    ID = 0x3637e05b
    QUALNAME = "functions.messages.GetSavedReactionTags"

    def __init__(self, *, hash: int, peer: "raw.base.InputPeer" = None) -> None:
        self.hash = hash  # long
        self.peer = peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedReactionTags":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 0) else None
        
        hash = Long.read(b)
        
        return GetSavedReactionTags(hash=hash, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.peer is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(Long(self.hash))
        
        return b.getvalue()
