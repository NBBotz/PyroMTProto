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


class ExportedChatlistInvite(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.chatlists.ExportedChatlistInvite`.

    Details:
        - Layer: ``227``
        - ID: ``10E6E3A6``

    Parameters:
        filter (:obj:`DialogFilter <pyrogram.raw.base.DialogFilter>`):
            N/A

        invite (:obj:`ExportedChatlistInvite <pyrogram.raw.base.ExportedChatlistInvite>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.ExportChatlistInvite
    """

    __slots__: list[str] = ["filter", "invite"]

    ID = 0x10e6e3a6
    QUALNAME = "types.chatlists.ExportedChatlistInvite"

    def __init__(self, *, filter: "raw.base.DialogFilter", invite: "raw.base.ExportedChatlistInvite") -> None:
        self.filter = filter  # DialogFilter
        self.invite = invite  # ExportedChatlistInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatlistInvite":
        # No flags
        
        filter = TLObject.read(b)
        
        invite = TLObject.read(b)
        
        return ExportedChatlistInvite(filter=filter, invite=invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.filter.write())
        
        b.write(self.invite.write())
        
        return b.getvalue()
