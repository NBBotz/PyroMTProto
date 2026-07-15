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


class ConnectedBot(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ConnectedBot`.

    Details:
        - Layer: ``227``
        - ID: ``33ED001``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        recipients (:obj:`BusinessBotRecipients <pyrogram.raw.base.BusinessBotRecipients>`):
            N/A

        rights (:obj:`BusinessBotRights <pyrogram.raw.base.BusinessBotRights>`):
            N/A

        device (``str``, *optional*):
            N/A

        date (``int`` ``32-bit``, *optional*):
            N/A

        location (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["bot_id", "recipients", "rights", "device", "date", "location"]

    ID = 0x33ed001
    QUALNAME = "types.ConnectedBot"

    def __init__(self, *, bot_id: int, recipients: "raw.base.BusinessBotRecipients", rights: "raw.base.BusinessBotRights", device: Optional[str] = None, date: Optional[int] = None, location: Optional[str] = None) -> None:
        self.bot_id = bot_id  # long
        self.recipients = recipients  # BusinessBotRecipients
        self.rights = rights  # BusinessBotRights
        self.device = device  # flags.0?string
        self.date = date  # flags.1?int
        self.location = location  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectedBot":
        
        flags = Int.read(b)
        
        bot_id = Long.read(b)
        
        recipients = TLObject.read(b)
        
        rights = TLObject.read(b)
        
        device = String.read(b) if flags & (1 << 0) else None
        date = Int.read(b) if flags & (1 << 1) else None
        location = String.read(b) if flags & (1 << 2) else None
        return ConnectedBot(bot_id=bot_id, recipients=recipients, rights=rights, device=device, date=date, location=location)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.device is not None else 0
        flags |= (1 << 1) if self.date is not None else 0
        flags |= (1 << 2) if self.location is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.bot_id))
        
        b.write(self.recipients.write())
        
        b.write(self.rights.write())
        
        if self.device is not None:
            b.write(String(self.device))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        if self.location is not None:
            b.write(String(self.location))
        
        return b.getvalue()
