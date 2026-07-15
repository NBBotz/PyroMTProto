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


class GetPeerMaxIDs(TLObject["List[raw.base.RecentStory]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``78499170``

    Parameters:
        id (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        List of :obj:`RecentStory <pyrogram.raw.base.RecentStory>`
    """

    __slots__: list[str] = ["id"]

    ID = 0x78499170
    QUALNAME = "functions.stories.GetPeerMaxIDs"

    def __init__(self, *, id: list["raw.base.InputPeer"]) -> None:
        self.id = id  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerMaxIDs":
        # No flags
        
        id = TLObject.read(b)
        
        return GetPeerMaxIDs(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()
