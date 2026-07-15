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


class UpdateColor(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``684D214E``

    Parameters:
        for_profile (``bool``, *optional*):
            N/A

        color (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["for_profile", "color"]

    ID = 0x684d214e
    QUALNAME = "functions.account.UpdateColor"

    def __init__(self, *, for_profile: Optional[bool] = None, color: "raw.base.PeerColor" = None) -> None:
        self.for_profile = for_profile  # flags.1?true
        self.color = color  # flags.2?PeerColor

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateColor":
        
        flags = Int.read(b)
        
        for_profile = True if flags & (1 << 1) else False
        color = TLObject.read(b) if flags & (1 << 2) else None
        
        return UpdateColor(for_profile=for_profile, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.for_profile else 0
        flags |= (1 << 2) if self.color is not None else 0
        b.write(Int(flags))
        
        if self.color is not None:
            b.write(self.color.write())
        
        return b.getvalue()
