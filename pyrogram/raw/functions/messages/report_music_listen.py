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


class ReportMusicListen(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``DDBCD819``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        listened_duration (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["id", "listened_duration"]

    ID = 0xddbcd819
    QUALNAME = "functions.messages.ReportMusicListen"

    def __init__(self, *, id: "raw.base.InputDocument", listened_duration: int) -> None:
        self.id = id  # InputDocument
        self.listened_duration = listened_duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportMusicListen":
        # No flags
        
        id = TLObject.read(b)
        
        listened_duration = Int.read(b)
        
        return ReportMusicListen(id=id, listened_duration=listened_duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(Int(self.listened_duration))
        
        return b.getvalue()
