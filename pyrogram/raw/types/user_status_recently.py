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


class UserStatusRecently(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.UserStatus`.

    Details:
        - Layer: ``227``
        - ID: ``7B197DC8``

    Parameters:
        by_me (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["by_me"]

    ID = 0x7b197dc8
    QUALNAME = "types.UserStatusRecently"

    def __init__(self, *, by_me: Optional[bool] = None) -> None:
        self.by_me = by_me  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserStatusRecently":
        
        flags = Int.read(b)
        
        by_me = True if flags & (1 << 0) else False
        return UserStatusRecently(by_me=by_me)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.by_me else 0
        b.write(Int(flags))
        
        return b.getvalue()
