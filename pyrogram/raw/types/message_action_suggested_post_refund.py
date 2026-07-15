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


class MessageActionSuggestedPostRefund(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``69F916F8``

    Parameters:
        payer_initiated (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["payer_initiated"]

    ID = 0x69f916f8
    QUALNAME = "types.MessageActionSuggestedPostRefund"

    def __init__(self, *, payer_initiated: Optional[bool] = None) -> None:
        self.payer_initiated = payer_initiated  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSuggestedPostRefund":
        
        flags = Int.read(b)
        
        payer_initiated = True if flags & (1 << 0) else False
        return MessageActionSuggestedPostRefund(payer_initiated=payer_initiated)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.payer_initiated else 0
        b.write(Int(flags))
        
        return b.getvalue()
