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


class PollAnswerVoters(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PollAnswerVoters`.

    Details:
        - Layer: ``227``
        - ID: ``3645230A``

    Parameters:
        option (``bytes``):
            N/A

        chosen (``bool``, *optional*):
            N/A

        correct (``bool``, *optional*):
            N/A

        voters (``int`` ``32-bit``, *optional*):
            N/A

        recent_voters (List of :obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["option", "chosen", "correct", "voters", "recent_voters"]

    ID = 0x3645230a
    QUALNAME = "types.PollAnswerVoters"

    def __init__(self, *, option: bytes, chosen: Optional[bool] = None, correct: Optional[bool] = None, voters: Optional[int] = None, recent_voters: Optional[list["raw.base.Peer"]] = None) -> None:
        self.option = option  # bytes
        self.chosen = chosen  # flags.0?true
        self.correct = correct  # flags.1?true
        self.voters = voters  # flags.2?int
        self.recent_voters = recent_voters  # flags.2?Vector<Peer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollAnswerVoters":
        
        flags = Int.read(b)
        
        chosen = True if flags & (1 << 0) else False
        correct = True if flags & (1 << 1) else False
        option = Bytes.read(b)
        
        voters = Int.read(b) if flags & (1 << 2) else None
        recent_voters = TLObject.read(b) if flags & (1 << 2) else []
        
        return PollAnswerVoters(option=option, chosen=chosen, correct=correct, voters=voters, recent_voters=recent_voters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.chosen else 0
        flags |= (1 << 1) if self.correct else 0
        flags |= (1 << 2) if self.voters is not None else 0
        flags |= (1 << 2) if self.recent_voters else 0
        b.write(Int(flags))
        
        b.write(Bytes(self.option))
        
        if self.voters is not None:
            b.write(Int(self.voters))
        
        if self.recent_voters is not None:
            b.write(Vector(self.recent_voters))
        
        return b.getvalue()
