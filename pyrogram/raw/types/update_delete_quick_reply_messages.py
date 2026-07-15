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


class UpdateDeleteQuickReplyMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``566FE7CD``

    Parameters:
        shortcut_id (``int`` ``32-bit``):
            N/A

        messages (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["shortcut_id", "messages"]

    ID = 0x566fe7cd
    QUALNAME = "types.UpdateDeleteQuickReplyMessages"

    def __init__(self, *, shortcut_id: int, messages: list[int]) -> None:
        self.shortcut_id = shortcut_id  # int
        self.messages = messages  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeleteQuickReplyMessages":
        # No flags
        
        shortcut_id = Int.read(b)
        
        messages = TLObject.read(b, Int)
        
        return UpdateDeleteQuickReplyMessages(shortcut_id=shortcut_id, messages=messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        b.write(Vector(self.messages, Int))
        
        return b.getvalue()
