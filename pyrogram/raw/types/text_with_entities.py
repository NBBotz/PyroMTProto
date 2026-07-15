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


class TextWithEntities(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TextWithEntities`.

    Details:
        - Layer: ``227``
        - ID: ``751F3146``

    Parameters:
        text (``str``):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SummarizeText
    """

    __slots__: list[str] = ["text", "entities"]

    ID = 0x751f3146
    QUALNAME = "types.TextWithEntities"

    def __init__(self, *, text: str, entities: list["raw.base.MessageEntity"]) -> None:
        self.text = text  # string
        self.entities = entities  # Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextWithEntities":
        # No flags
        
        text = String.read(b)
        
        entities = TLObject.read(b)
        
        return TextWithEntities(text=text, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(Vector(self.entities))
        
        return b.getvalue()
