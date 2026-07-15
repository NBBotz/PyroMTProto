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


class UpdateChatParticipants(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``7761198``

    Parameters:
        participants (:obj:`ChatParticipants <pyrogram.raw.base.ChatParticipants>`):
            N/A

    """

    __slots__: list[str] = ["participants"]

    ID = 0x7761198
    QUALNAME = "types.UpdateChatParticipants"

    def __init__(self, *, participants: "raw.base.ChatParticipants") -> None:
        self.participants = participants  # ChatParticipants

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipants":
        # No flags
        
        participants = TLObject.read(b)
        
        return UpdateChatParticipants(participants=participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.participants.write())
        
        return b.getvalue()
