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


class MessageActionSetMessagesTTL(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``3C134D7B``

    Parameters:
        period (``int`` ``32-bit``):
            N/A

        auto_setting_from (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["period", "auto_setting_from"]

    ID = 0x3c134d7b
    QUALNAME = "types.MessageActionSetMessagesTTL"

    def __init__(self, *, period: int, auto_setting_from: Optional[int] = None) -> None:
        self.period = period  # int
        self.auto_setting_from = auto_setting_from  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetMessagesTTL":
        
        flags = Int.read(b)
        
        period = Int.read(b)
        
        auto_setting_from = Long.read(b) if flags & (1 << 0) else None
        return MessageActionSetMessagesTTL(period=period, auto_setting_from=auto_setting_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.auto_setting_from is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.period))
        
        if self.auto_setting_from is not None:
            b.write(Long(self.auto_setting_from))
        
        return b.getvalue()
