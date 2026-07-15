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


class InputMessagesFilterPhoneCalls(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessagesFilter`.

    Details:
        - Layer: ``227``
        - ID: ``80C99768``

    Parameters:
        missed (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["missed"]

    ID = 0x80c99768
    QUALNAME = "types.InputMessagesFilterPhoneCalls"

    def __init__(self, *, missed: Optional[bool] = None) -> None:
        self.missed = missed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessagesFilterPhoneCalls":
        
        flags = Int.read(b)
        
        missed = True if flags & (1 << 0) else False
        return InputMessagesFilterPhoneCalls(missed=missed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.missed else 0
        b.write(Int(flags))
        
        return b.getvalue()
