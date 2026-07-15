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


class ChatReactionsAll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatReactions`.

    Details:
        - Layer: ``227``
        - ID: ``52928BCA``

    Parameters:
        allow_custom (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["allow_custom"]

    ID = 0x52928bca
    QUALNAME = "types.ChatReactionsAll"

    def __init__(self, *, allow_custom: Optional[bool] = None) -> None:
        self.allow_custom = allow_custom  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatReactionsAll":
        
        flags = Int.read(b)
        
        allow_custom = True if flags & (1 << 0) else False
        return ChatReactionsAll(allow_custom=allow_custom)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_custom else 0
        b.write(Int(flags))
        
        return b.getvalue()
