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


class ReceivedNotifyMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReceivedNotifyMessage`.

    Details:
        - Layer: ``227``
        - ID: ``A384B779``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        flags (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReceivedMessages
    """

    __slots__: list[str] = ["id", "flags"]

    ID = 0xa384b779
    QUALNAME = "types.ReceivedNotifyMessage"

    def __init__(self, *, id: int, flags: int) -> None:
        self.id = id  # int
        self.flags = flags  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedNotifyMessage":
        # No flags
        
        id = Int.read(b)
        
        flags = Int.read(b)
        
        return ReceivedNotifyMessage(id=id, flags=flags)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(Int(self.flags))
        
        return b.getvalue()
