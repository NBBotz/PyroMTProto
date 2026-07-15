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


class ChannelAdminLogEventActionParticipantJoinByRequest(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``227``
        - ID: ``AFB6144A``

    Parameters:
        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            N/A

        approved_by (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["invite", "approved_by"]

    ID = 0xafb6144a
    QUALNAME = "types.ChannelAdminLogEventActionParticipantJoinByRequest"

    def __init__(self, *, invite: "raw.base.ExportedChatInvite", approved_by: int) -> None:
        self.invite = invite  # ExportedChatInvite
        self.approved_by = approved_by  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantJoinByRequest":
        # No flags
        
        invite = TLObject.read(b)
        
        approved_by = Long.read(b)
        
        return ChannelAdminLogEventActionParticipantJoinByRequest(invite=invite, approved_by=approved_by)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.invite.write())
        
        b.write(Long(self.approved_by))
        
        return b.getvalue()
