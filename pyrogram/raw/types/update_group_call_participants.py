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


class UpdateGroupCallParticipants(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``F2EBDB4E``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        participants (List of :obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["call", "participants", "version"]

    ID = 0xf2ebdb4e
    QUALNAME = "types.UpdateGroupCallParticipants"

    def __init__(self, *, call: "raw.base.InputGroupCall", participants: list["raw.base.GroupCallParticipant"], version: int) -> None:
        self.call = call  # InputGroupCall
        self.participants = participants  # Vector<GroupCallParticipant>
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallParticipants":
        # No flags
        
        call = TLObject.read(b)
        
        participants = TLObject.read(b)
        
        version = Int.read(b)
        
        return UpdateGroupCallParticipants(call=call, participants=participants, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Vector(self.participants))
        
        b.write(Int(self.version))
        
        return b.getvalue()
