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


class AccessSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.bots.AccessSettings`.

    Details:
        - Layer: ``227``
        - ID: ``DD1FBF93``

    Parameters:
        restricted (``bool``, *optional*):
            N/A

        add_users (List of :obj:`User <pyrogram.raw.base.User>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetAccessSettings
    """

    __slots__: list[str] = ["restricted", "add_users"]

    ID = 0xdd1fbf93
    QUALNAME = "types.bots.AccessSettings"

    def __init__(self, *, restricted: Optional[bool] = None, add_users: Optional[list["raw.base.User"]] = None) -> None:
        self.restricted = restricted  # flags.0?true
        self.add_users = add_users  # flags.1?Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AccessSettings":
        
        flags = Int.read(b)
        
        restricted = True if flags & (1 << 0) else False
        add_users = TLObject.read(b) if flags & (1 << 1) else []
        
        return AccessSettings(restricted=restricted, add_users=add_users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.restricted else 0
        flags |= (1 << 1) if self.add_users else 0
        b.write(Int(flags))
        
        if self.add_users is not None:
            b.write(Vector(self.add_users))
        
        return b.getvalue()
