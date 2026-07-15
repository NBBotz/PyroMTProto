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


class UpdateBotNewBusinessMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``9DDB347C``

    Parameters:
        connection_id (``str``):
            N/A

        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

        reply_to_message (:obj:`Message <pyrogram.raw.base.Message>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["connection_id", "message", "qts", "reply_to_message"]

    ID = 0x9ddb347c
    QUALNAME = "types.UpdateBotNewBusinessMessage"

    def __init__(self, *, connection_id: str, message: "raw.base.Message", qts: int, reply_to_message: "raw.base.Message" = None) -> None:
        self.connection_id = connection_id  # string
        self.message = message  # Message
        self.qts = qts  # int
        self.reply_to_message = reply_to_message  # flags.0?Message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotNewBusinessMessage":
        
        flags = Int.read(b)
        
        connection_id = String.read(b)
        
        message = TLObject.read(b)
        
        reply_to_message = TLObject.read(b) if flags & (1 << 0) else None
        
        qts = Int.read(b)
        
        return UpdateBotNewBusinessMessage(connection_id=connection_id, message=message, qts=qts, reply_to_message=reply_to_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reply_to_message is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.connection_id))
        
        b.write(self.message.write())
        
        if self.reply_to_message is not None:
            b.write(self.reply_to_message.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
