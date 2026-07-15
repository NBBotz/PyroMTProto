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


class SendMessageUploadVideoAction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``E9763AEC``

    Parameters:
        progress (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["progress"]

    ID = 0xe9763aec
    QUALNAME = "types.SendMessageUploadVideoAction"

    def __init__(self, *, progress: int) -> None:
        self.progress = progress  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageUploadVideoAction":
        # No flags
        
        progress = Int.read(b)
        
        return SendMessageUploadVideoAction(progress=progress)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.progress))
        
        return b.getvalue()
