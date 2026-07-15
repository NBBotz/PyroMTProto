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


class GetGroupCallStreamRtmpUrl(TLObject["raw.base.phone.GroupCallStreamRtmpUrl"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``5AF4C73A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        revoke (``bool``):
            N/A

        live_story (``bool``, *optional*):
            N/A

    Returns:
        :obj:`phone.GroupCallStreamRtmpUrl <pyrogram.raw.base.phone.GroupCallStreamRtmpUrl>`
    """

    __slots__: list[str] = ["peer", "revoke", "live_story"]

    ID = 0x5af4c73a
    QUALNAME = "functions.phone.GetGroupCallStreamRtmpUrl"

    def __init__(self, *, peer: "raw.base.InputPeer", revoke: bool, live_story: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.revoke = revoke  # Bool
        self.live_story = live_story  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallStreamRtmpUrl":
        
        flags = Int.read(b)
        
        live_story = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        revoke = Bool.read(b)
        
        return GetGroupCallStreamRtmpUrl(peer=peer, revoke=revoke, live_story=live_story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.live_story else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Bool(self.revoke))
        
        return b.getvalue()
