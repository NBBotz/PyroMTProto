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


class MessageMediaDice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``227``
        - ID: ``8CBEC07``

    Parameters:
        value (``int`` ``32-bit``):
            N/A

        emoticon (``str``):
            N/A

        game_outcome (:obj:`messages.EmojiGameOutcome <pyrogram.raw.base.messages.EmojiGameOutcome>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: list[str] = ["value", "emoticon", "game_outcome"]

    ID = 0x8cbec07
    QUALNAME = "types.MessageMediaDice"

    def __init__(self, *, value: int, emoticon: str, game_outcome: "raw.base.messages.EmojiGameOutcome" = None) -> None:
        self.value = value  # int
        self.emoticon = emoticon  # string
        self.game_outcome = game_outcome  # flags.0?messages.EmojiGameOutcome

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaDice":
        
        flags = Int.read(b)
        
        value = Int.read(b)
        
        emoticon = String.read(b)
        
        game_outcome = TLObject.read(b) if flags & (1 << 0) else None
        
        return MessageMediaDice(value=value, emoticon=emoticon, game_outcome=game_outcome)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.game_outcome is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.value))
        
        b.write(String(self.emoticon))
        
        if self.game_outcome is not None:
            b.write(self.game_outcome.write())
        
        return b.getvalue()
