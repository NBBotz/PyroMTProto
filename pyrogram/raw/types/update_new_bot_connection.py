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


class UpdateNewBotConnection(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``B22083A6``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        confirmed (``bool``, *optional*):
            N/A

        date (``int`` ``32-bit``, *optional*):
            N/A

        device (``str``, *optional*):
            N/A

        location (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["bot_id", "confirmed", "date", "device", "location"]

    ID = 0xb22083a6
    QUALNAME = "types.UpdateNewBotConnection"

    def __init__(self, *, bot_id: int, confirmed: Optional[bool] = None, date: Optional[int] = None, device: Optional[str] = None, location: Optional[str] = None) -> None:
        self.bot_id = bot_id  # long
        self.confirmed = confirmed  # flags.0?true
        self.date = date  # flags.1?int
        self.device = device  # flags.1?string
        self.location = location  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewBotConnection":
        
        flags = Int.read(b)
        
        confirmed = True if flags & (1 << 0) else False
        bot_id = Long.read(b)
        
        date = Int.read(b) if flags & (1 << 1) else None
        device = String.read(b) if flags & (1 << 1) else None
        location = String.read(b) if flags & (1 << 1) else None
        return UpdateNewBotConnection(bot_id=bot_id, confirmed=confirmed, date=date, device=device, location=location)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.confirmed else 0
        flags |= (1 << 1) if self.date is not None else 0
        flags |= (1 << 1) if self.device is not None else 0
        flags |= (1 << 1) if self.location is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.bot_id))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        if self.device is not None:
            b.write(String(self.device))
        
        if self.location is not None:
            b.write(String(self.location))
        
        return b.getvalue()
