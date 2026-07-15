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


class MessageActionGroupCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``7A0D7F42``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        duration (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["call", "duration"]

    ID = 0x7a0d7f42
    QUALNAME = "types.MessageActionGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", duration: Optional[int] = None) -> None:
        self.call = call  # InputGroupCall
        self.duration = duration  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGroupCall":
        
        flags = Int.read(b)
        
        call = TLObject.read(b)
        
        duration = Int.read(b) if flags & (1 << 0) else None
        return MessageActionGroupCall(call=call, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.duration is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()
