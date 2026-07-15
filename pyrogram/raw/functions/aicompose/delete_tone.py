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


class DeleteTone(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``DD39316A``

    Parameters:
        tone (:obj:`InputAiComposeTone <pyrogram.raw.base.InputAiComposeTone>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["tone"]

    ID = 0xdd39316a
    QUALNAME = "functions.aicompose.DeleteTone"

    def __init__(self, *, tone: "raw.base.InputAiComposeTone") -> None:
        self.tone = tone  # InputAiComposeTone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteTone":
        # No flags
        
        tone = TLObject.read(b)
        
        return DeleteTone(tone=tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.tone.write())
        
        return b.getvalue()
