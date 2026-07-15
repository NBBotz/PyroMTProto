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


class MessageActionGiveawayLaunch(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``A80F51E4``

    Parameters:
        stars (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["stars"]

    ID = 0xa80f51e4
    QUALNAME = "types.MessageActionGiveawayLaunch"

    def __init__(self, *, stars: Optional[int] = None) -> None:
        self.stars = stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiveawayLaunch":
        
        flags = Int.read(b)
        
        stars = Long.read(b) if flags & (1 << 0) else None
        return MessageActionGiveawayLaunch(stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.stars is not None else 0
        b.write(Int(flags))
        
        if self.stars is not None:
            b.write(Long(self.stars))
        
        return b.getvalue()
