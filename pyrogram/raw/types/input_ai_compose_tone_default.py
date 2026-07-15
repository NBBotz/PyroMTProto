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


class InputAiComposeToneDefault(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputAiComposeTone`.

    Details:
        - Layer: ``227``
        - ID: ``1FE9A9BF``

    Parameters:
        tone (``str``):
            N/A

    """

    __slots__: list[str] = ["tone"]

    ID = 0x1fe9a9bf
    QUALNAME = "types.InputAiComposeToneDefault"

    def __init__(self, *, tone: str) -> None:
        self.tone = tone  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputAiComposeToneDefault":
        # No flags
        
        tone = String.read(b)
        
        return InputAiComposeToneDefault(tone=tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.tone))
        
        return b.getvalue()
