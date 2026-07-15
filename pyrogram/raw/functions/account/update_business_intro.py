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


class UpdateBusinessIntro(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``A614D034``

    Parameters:
        intro (:obj:`InputBusinessIntro <pyrogram.raw.base.InputBusinessIntro>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["intro"]

    ID = 0xa614d034
    QUALNAME = "functions.account.UpdateBusinessIntro"

    def __init__(self, *, intro: "raw.base.InputBusinessIntro" = None) -> None:
        self.intro = intro  # flags.0?InputBusinessIntro

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessIntro":
        
        flags = Int.read(b)
        
        intro = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessIntro(intro=intro)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.intro is not None else 0
        b.write(Int(flags))
        
        if self.intro is not None:
            b.write(self.intro.write())
        
        return b.getvalue()
