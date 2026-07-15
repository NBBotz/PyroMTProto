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


class UpdateUserName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``A7848924``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        first_name (``str``):
            N/A

        last_name (``str``):
            N/A

        usernames (List of :obj:`Username <pyrogram.raw.base.Username>`):
            N/A

    """

    __slots__: list[str] = ["user_id", "first_name", "last_name", "usernames"]

    ID = 0xa7848924
    QUALNAME = "types.UpdateUserName"

    def __init__(self, *, user_id: int, first_name: str, last_name: str, usernames: list["raw.base.Username"]) -> None:
        self.user_id = user_id  # long
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.usernames = usernames  # Vector<Username>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserName":
        # No flags
        
        user_id = Long.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        usernames = TLObject.read(b)
        
        return UpdateUserName(user_id=user_id, first_name=first_name, last_name=last_name, usernames=usernames)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(Vector(self.usernames))
        
        return b.getvalue()
