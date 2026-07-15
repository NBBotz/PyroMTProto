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


class TranslateResult(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.TranslatedText`.

    Details:
        - Layer: ``227``
        - ID: ``33DB32F8``

    Parameters:
        result (List of :obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.TranslateText
    """

    __slots__: list[str] = ["result"]

    ID = 0x33db32f8
    QUALNAME = "types.messages.TranslateResult"

    def __init__(self, *, result: list["raw.base.TextWithEntities"]) -> None:
        self.result = result  # Vector<TextWithEntities>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranslateResult":
        # No flags
        
        result = TLObject.read(b)
        
        return TranslateResult(result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.result))
        
        return b.getvalue()
