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


class UpdateQuickReplies(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``F9470AB2``

    Parameters:
        quick_replies (List of :obj:`QuickReply <pyrogram.raw.base.QuickReply>`):
            N/A

    """

    __slots__: list[str] = ["quick_replies"]

    ID = 0xf9470ab2
    QUALNAME = "types.UpdateQuickReplies"

    def __init__(self, *, quick_replies: list["raw.base.QuickReply"]) -> None:
        self.quick_replies = quick_replies  # Vector<QuickReply>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateQuickReplies":
        # No flags
        
        quick_replies = TLObject.read(b)
        
        return UpdateQuickReplies(quick_replies=quick_replies)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.quick_replies))
        
        return b.getvalue()
