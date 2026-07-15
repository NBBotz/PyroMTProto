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


class UpdateBusinessAwayMessage(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``A26A7FA5``

    Parameters:
        message (:obj:`InputBusinessAwayMessage <pyrogram.raw.base.InputBusinessAwayMessage>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["message"]

    ID = 0xa26a7fa5
    QUALNAME = "functions.account.UpdateBusinessAwayMessage"

    def __init__(self, *, message: "raw.base.InputBusinessAwayMessage" = None) -> None:
        self.message = message  # flags.0?InputBusinessAwayMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessAwayMessage":
        
        flags = Int.read(b)
        
        message = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessAwayMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message is not None else 0
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
