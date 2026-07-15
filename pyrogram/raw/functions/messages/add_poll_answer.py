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


class AddPollAnswer(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``19BC4B6D``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        answer (:obj:`PollAnswer <pyrogram.raw.base.PollAnswer>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = ["peer", "msg_id", "answer"]

    ID = 0x19bc4b6d
    QUALNAME = "functions.messages.AddPollAnswer"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, answer: "raw.base.PollAnswer") -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.answer = answer  # PollAnswer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddPollAnswer":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        answer = TLObject.read(b)
        
        return AddPollAnswer(peer=peer, msg_id=msg_id, answer=answer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(self.answer.write())
        
        return b.getvalue()
