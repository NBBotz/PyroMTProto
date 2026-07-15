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


class SponsoredPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SponsoredPeer`.

    Details:
        - Layer: ``227``
        - ID: ``C69708D3``

    Parameters:
        random_id (``bytes``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        sponsor_info (``str``, *optional*):
            N/A

        additional_info (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["random_id", "peer", "sponsor_info", "additional_info"]

    ID = 0xc69708d3
    QUALNAME = "types.SponsoredPeer"

    def __init__(self, *, random_id: bytes, peer: "raw.base.Peer", sponsor_info: Optional[str] = None, additional_info: Optional[str] = None) -> None:
        self.random_id = random_id  # bytes
        self.peer = peer  # Peer
        self.sponsor_info = sponsor_info  # flags.0?string
        self.additional_info = additional_info  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredPeer":
        
        flags = Int.read(b)
        
        random_id = Bytes.read(b)
        
        peer = TLObject.read(b)
        
        sponsor_info = String.read(b) if flags & (1 << 0) else None
        additional_info = String.read(b) if flags & (1 << 1) else None
        return SponsoredPeer(random_id=random_id, peer=peer, sponsor_info=sponsor_info, additional_info=additional_info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sponsor_info is not None else 0
        flags |= (1 << 1) if self.additional_info is not None else 0
        b.write(Int(flags))
        
        b.write(Bytes(self.random_id))
        
        b.write(self.peer.write())
        
        if self.sponsor_info is not None:
            b.write(String(self.sponsor_info))
        
        if self.additional_info is not None:
            b.write(String(self.additional_info))
        
        return b.getvalue()
