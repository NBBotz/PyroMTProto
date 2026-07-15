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


class GetToneExample(TLObject["raw.base.AiComposeToneExample"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``D1B4AB14``

    Parameters:
        tone (:obj:`InputAiComposeTone <pyrogram.raw.base.InputAiComposeTone>`):
            N/A

        num (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`AiComposeToneExample <pyrogram.raw.base.AiComposeToneExample>`
    """

    __slots__: list[str] = ["tone", "num"]

    ID = 0xd1b4ab14
    QUALNAME = "functions.aicompose.GetToneExample"

    def __init__(self, *, tone: "raw.base.InputAiComposeTone", num: int) -> None:
        self.tone = tone  # InputAiComposeTone
        self.num = num  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetToneExample":
        # No flags
        
        tone = TLObject.read(b)
        
        num = Int.read(b)
        
        return GetToneExample(tone=tone, num=num)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.tone.write())
        
        b.write(Int(self.num))
        
        return b.getvalue()
