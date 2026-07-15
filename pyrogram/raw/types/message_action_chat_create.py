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


class MessageActionChatCreate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``BD47CBAD``

    Parameters:
        title (``str``):
            N/A

        users (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["title", "users"]

    ID = 0xbd47cbad
    QUALNAME = "types.MessageActionChatCreate"

    def __init__(self, *, title: str, users: list[int]) -> None:
        self.title = title  # string
        self.users = users  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatCreate":
        # No flags
        
        title = String.read(b)
        
        users = TLObject.read(b, Long)
        
        return MessageActionChatCreate(title=title, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Vector(self.users, Long))
        
        return b.getvalue()
