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


class SendMessageRichMessageDraftAction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``A2CB24F9``

    Parameters:
        random_id (``int`` ``64-bit``):
            N/A

        rich_message (:obj:`RichMessage <pyrogram.raw.base.RichMessage>`):
            N/A

    """

    __slots__: list[str] = ["random_id", "rich_message"]

    ID = 0xa2cb24f9
    QUALNAME = "types.SendMessageRichMessageDraftAction"

    def __init__(self, *, random_id: int, rich_message: "raw.base.RichMessage") -> None:
        self.random_id = random_id  # long
        self.rich_message = rich_message  # RichMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageRichMessageDraftAction":
        # No flags
        
        random_id = Long.read(b)
        
        rich_message = TLObject.read(b)
        
        return SendMessageRichMessageDraftAction(random_id=random_id, rich_message=rich_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.random_id))
        
        b.write(self.rich_message.write())
        
        return b.getvalue()
