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


class InputChatlistDialogFilter(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputChatlist`.

    Details:
        - Layer: ``227``
        - ID: ``F3E0DA33``

    Parameters:
        filter_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["filter_id"]

    ID = 0xf3e0da33
    QUALNAME = "types.InputChatlistDialogFilter"

    def __init__(self, *, filter_id: int) -> None:
        self.filter_id = filter_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatlistDialogFilter":
        # No flags
        
        filter_id = Int.read(b)
        
        return InputChatlistDialogFilter(filter_id=filter_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.filter_id))
        
        return b.getvalue()
