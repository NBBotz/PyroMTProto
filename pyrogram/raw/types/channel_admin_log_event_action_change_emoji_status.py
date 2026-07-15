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


class ChannelAdminLogEventActionChangeEmojiStatus(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``227``
        - ID: ``3EA9FEB1``

    Parameters:
        prev_value (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            N/A

        new_value (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            N/A

    """

    __slots__: list[str] = ["prev_value", "new_value"]

    ID = 0x3ea9feb1
    QUALNAME = "types.ChannelAdminLogEventActionChangeEmojiStatus"

    def __init__(self, *, prev_value: "raw.base.EmojiStatus", new_value: "raw.base.EmojiStatus") -> None:
        self.prev_value = prev_value  # EmojiStatus
        self.new_value = new_value  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeEmojiStatus":
        # No flags
        
        prev_value = TLObject.read(b)
        
        new_value = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangeEmojiStatus(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()
