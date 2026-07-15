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


class GetTone(TLObject["raw.base.aicompose.Tones"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``B2E8BA03``

    Parameters:
        tone (:obj:`InputAiComposeTone <pyrogram.raw.base.InputAiComposeTone>`):
            N/A

    Returns:
        :obj:`aicompose.Tones <pyrogram.raw.base.aicompose.Tones>`
    """

    __slots__: list[str] = ["tone"]

    ID = 0xb2e8ba03
    QUALNAME = "functions.aicompose.GetTone"

    def __init__(self, *, tone: "raw.base.InputAiComposeTone") -> None:
        self.tone = tone  # InputAiComposeTone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTone":
        # No flags
        
        tone = TLObject.read(b)
        
        return GetTone(tone=tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.tone.write())
        
        return b.getvalue()
