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


class InputStarsTransaction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStarsTransaction`.

    Details:
        - Layer: ``227``
        - ID: ``206AE6D1``

    Parameters:
        id (``str``):
            N/A

        refund (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "refund"]

    ID = 0x206ae6d1
    QUALNAME = "types.InputStarsTransaction"

    def __init__(self, *, id: str, refund: Optional[bool] = None) -> None:
        self.id = id  # string
        self.refund = refund  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStarsTransaction":
        
        flags = Int.read(b)
        
        refund = True if flags & (1 << 0) else False
        id = String.read(b)
        
        return InputStarsTransaction(id=id, refund=refund)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.refund else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        return b.getvalue()
