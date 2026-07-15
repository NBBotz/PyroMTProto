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


class GetPinnedDialogs(TLObject["raw.base.messages.PeerDialogs"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``D6B94DF2``

    Parameters:
        folder_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.PeerDialogs <pyrogram.raw.base.messages.PeerDialogs>`
    """

    __slots__: list[str] = ["folder_id"]

    ID = 0xd6b94df2
    QUALNAME = "functions.messages.GetPinnedDialogs"

    def __init__(self, *, folder_id: int) -> None:
        self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPinnedDialogs":
        # No flags
        
        folder_id = Int.read(b)
        
        return GetPinnedDialogs(folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.folder_id))
        
        return b.getvalue()
