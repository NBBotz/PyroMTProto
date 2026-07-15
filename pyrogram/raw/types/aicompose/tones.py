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


class Tones(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.aicompose.Tones`.

    Details:
        - Layer: ``227``
        - ID: ``6C9D0EFE``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        tones (List of :obj:`AiComposeTone <pyrogram.raw.base.AiComposeTone>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            aicompose.GetTone
            aicompose.GetTones
    """

    __slots__: list[str] = ["hash", "tones", "users"]

    ID = 0x6c9d0efe
    QUALNAME = "types.aicompose.Tones"

    def __init__(self, *, hash: int, tones: list["raw.base.AiComposeTone"], users: list["raw.base.User"]) -> None:
        self.hash = hash  # long
        self.tones = tones  # Vector<AiComposeTone>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Tones":
        # No flags
        
        hash = Long.read(b)
        
        tones = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Tones(hash=hash, tones=tones, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.tones))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
