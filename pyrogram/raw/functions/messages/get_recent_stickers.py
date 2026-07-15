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


class GetRecentStickers(TLObject["raw.base.messages.RecentStickers"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``9DA9403B``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        attached (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.RecentStickers <pyrogram.raw.base.messages.RecentStickers>`
    """

    __slots__: list[str] = ["hash", "attached"]

    ID = 0x9da9403b
    QUALNAME = "functions.messages.GetRecentStickers"

    def __init__(self, *, hash: int, attached: Optional[bool] = None) -> None:
        self.hash = hash  # long
        self.attached = attached  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentStickers":
        
        flags = Int.read(b)
        
        attached = True if flags & (1 << 0) else False
        hash = Long.read(b)
        
        return GetRecentStickers(hash=hash, attached=attached)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached else 0
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
