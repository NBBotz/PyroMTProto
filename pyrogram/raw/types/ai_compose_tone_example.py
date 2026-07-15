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


class AiComposeToneExample(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AiComposeToneExample`.

    Details:
        - Layer: ``227``
        - ID: ``F1D628EC``

    Parameters:
        is_from (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        to (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            aicompose.GetToneExample
    """

    __slots__: list[str] = ["is_from", "to"]

    ID = 0xf1d628ec
    QUALNAME = "types.AiComposeToneExample"

    def __init__(self, *, is_from: "raw.base.TextWithEntities", to: "raw.base.TextWithEntities") -> None:
        self.is_from = is_from  # TextWithEntities
        self.to = to  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AiComposeToneExample":
        # No flags
        
        is_from = TLObject.read(b)
        
        to = TLObject.read(b)
        
        return AiComposeToneExample(is_from=is_from, to=to)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.is_from.write())
        
        b.write(self.to.write())
        
        return b.getvalue()
