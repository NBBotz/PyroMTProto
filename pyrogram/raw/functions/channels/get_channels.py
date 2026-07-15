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


class GetChannels(TLObject["raw.base.messages.Chats"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``A7F6BBB``

    Parameters:
        id (List of :obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: list[str] = ["id"]

    ID = 0xa7f6bbb
    QUALNAME = "functions.channels.GetChannels"

    def __init__(self, *, id: list["raw.base.InputChannel"]) -> None:
        self.id = id  # Vector<InputChannel>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannels":
        # No flags
        
        id = TLObject.read(b)
        
        return GetChannels(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()
