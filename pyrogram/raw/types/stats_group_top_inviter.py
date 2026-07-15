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


class StatsGroupTopInviter(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StatsGroupTopInviter`.

    Details:
        - Layer: ``227``
        - ID: ``535F779D``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        invitations (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["user_id", "invitations"]

    ID = 0x535f779d
    QUALNAME = "types.StatsGroupTopInviter"

    def __init__(self, *, user_id: int, invitations: int) -> None:
        self.user_id = user_id  # long
        self.invitations = invitations  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGroupTopInviter":
        # No flags
        
        user_id = Long.read(b)
        
        invitations = Int.read(b)
        
        return StatsGroupTopInviter(user_id=user_id, invitations=invitations)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.invitations))
        
        return b.getvalue()
