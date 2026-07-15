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


class HighScore(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.HighScore`.

    Details:
        - Layer: ``227``
        - ID: ``73A379EB``

    Parameters:
        pos (``int`` ``32-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        score (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["pos", "user_id", "score"]

    ID = 0x73a379eb
    QUALNAME = "types.HighScore"

    def __init__(self, *, pos: int, user_id: int, score: int) -> None:
        self.pos = pos  # int
        self.user_id = user_id  # long
        self.score = score  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HighScore":
        # No flags
        
        pos = Int.read(b)
        
        user_id = Long.read(b)
        
        score = Int.read(b)
        
        return HighScore(pos=pos, user_id=user_id, score=score)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pos))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.score))
        
        return b.getvalue()
