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


class ChannelParticipantBanned(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``227``
        - ID: ``D5F0AD91``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        kicked_by (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            N/A

        left (``bool``, *optional*):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer", "kicked_by", "date", "banned_rights", "left", "rank"]

    ID = 0xd5f0ad91
    QUALNAME = "types.ChannelParticipantBanned"

    def __init__(self, *, peer: "raw.base.Peer", kicked_by: int, date: int, banned_rights: "raw.base.ChatBannedRights", left: Optional[bool] = None, rank: Optional[str] = None) -> None:
        self.peer = peer  # Peer
        self.kicked_by = kicked_by  # long
        self.date = date  # int
        self.banned_rights = banned_rights  # ChatBannedRights
        self.left = left  # flags.0?true
        self.rank = rank  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantBanned":
        
        flags = Int.read(b)
        
        left = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        kicked_by = Long.read(b)
        
        date = Int.read(b)
        
        banned_rights = TLObject.read(b)
        
        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipantBanned(peer=peer, kicked_by=kicked_by, date=date, banned_rights=banned_rights, left=left, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.left else 0
        flags |= (1 << 2) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.kicked_by))
        
        b.write(Int(self.date))
        
        b.write(self.banned_rights.write())
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()
