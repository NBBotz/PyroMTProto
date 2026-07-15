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


class UpdateBotGuestChatQuery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``CDD4093D``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

        reference_messages (List of :obj:`Message <pyrogram.raw.base.Message>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["query_id", "message", "qts", "reference_messages"]

    ID = 0xcdd4093d
    QUALNAME = "types.UpdateBotGuestChatQuery"

    def __init__(self, *, query_id: int, message: "raw.base.Message", qts: int, reference_messages: Optional[list["raw.base.Message"]] = None) -> None:
        self.query_id = query_id  # long
        self.message = message  # Message
        self.qts = qts  # int
        self.reference_messages = reference_messages  # flags.0?Vector<Message>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotGuestChatQuery":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        message = TLObject.read(b)
        
        reference_messages = TLObject.read(b) if flags & (1 << 0) else []
        
        qts = Int.read(b)
        
        return UpdateBotGuestChatQuery(query_id=query_id, message=message, qts=qts, reference_messages=reference_messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reference_messages else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(self.message.write())
        
        if self.reference_messages is not None:
            b.write(Vector(self.reference_messages))
        
        b.write(Int(self.qts))
        
        return b.getvalue()
