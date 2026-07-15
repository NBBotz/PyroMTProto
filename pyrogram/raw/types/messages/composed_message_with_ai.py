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


class ComposedMessageWithAI(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ComposedMessageWithAI`.

    Details:
        - Layer: ``227``
        - ID: ``90D7ADFA``

    Parameters:
        result_text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        diff_text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ComposeMessageWithAI
    """

    __slots__: list[str] = ["result_text", "diff_text"]

    ID = 0x90d7adfa
    QUALNAME = "types.messages.ComposedMessageWithAI"

    def __init__(self, *, result_text: "raw.base.TextWithEntities", diff_text: "raw.base.TextWithEntities" = None) -> None:
        self.result_text = result_text  # TextWithEntities
        self.diff_text = diff_text  # flags.0?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ComposedMessageWithAI":
        
        flags = Int.read(b)
        
        result_text = TLObject.read(b)
        
        diff_text = TLObject.read(b) if flags & (1 << 0) else None
        
        return ComposedMessageWithAI(result_text=result_text, diff_text=diff_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.diff_text is not None else 0
        b.write(Int(flags))
        
        b.write(self.result_text.write())
        
        if self.diff_text is not None:
            b.write(self.diff_text.write())
        
        return b.getvalue()
