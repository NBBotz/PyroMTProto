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


class MessageReplyStoryHeader(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageReplyHeader`.

    Details:
        - Layer: ``227``
        - ID: ``E5AF939``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        story_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["peer", "story_id"]

    ID = 0xe5af939
    QUALNAME = "types.MessageReplyStoryHeader"

    def __init__(self, *, peer: "raw.base.Peer", story_id: int) -> None:
        self.peer = peer  # Peer
        self.story_id = story_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplyStoryHeader":
        # No flags
        
        peer = TLObject.read(b)
        
        story_id = Int.read(b)
        
        return MessageReplyStoryHeader(peer=peer, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.story_id))
        
        return b.getvalue()
