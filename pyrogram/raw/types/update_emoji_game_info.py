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


class UpdateEmojiGameInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``FB9C547A``

    Parameters:
        info (:obj:`messages.EmojiGameInfo <pyrogram.raw.base.messages.EmojiGameInfo>`):
            N/A

    """

    __slots__: list[str] = ["info"]

    ID = 0xfb9c547a
    QUALNAME = "types.UpdateEmojiGameInfo"

    def __init__(self, *, info: "raw.base.messages.EmojiGameInfo") -> None:
        self.info = info  # messages.EmojiGameInfo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEmojiGameInfo":
        # No flags
        
        info = TLObject.read(b)
        
        return UpdateEmojiGameInfo(info=info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.info.write())
        
        return b.getvalue()
