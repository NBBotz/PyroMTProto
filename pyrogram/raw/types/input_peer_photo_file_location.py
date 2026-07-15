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


class InputPeerPhotoFileLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``227``
        - ID: ``37257E99``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        photo_id (``int`` ``64-bit``):
            N/A

        big (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer", "photo_id", "big"]

    ID = 0x37257e99
    QUALNAME = "types.InputPeerPhotoFileLocation"

    def __init__(self, *, peer: "raw.base.InputPeer", photo_id: int, big: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.photo_id = photo_id  # long
        self.big = big  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerPhotoFileLocation":
        
        flags = Int.read(b)
        
        big = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        photo_id = Long.read(b)
        
        return InputPeerPhotoFileLocation(peer=peer, photo_id=photo_id, big=big)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.photo_id))
        
        return b.getvalue()
