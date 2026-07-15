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


class PendingSuggestion(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PendingSuggestion`.

    Details:
        - Layer: ``227``
        - ID: ``E7E82E12``

    Parameters:
        suggestion (``str``):
            N/A

        title (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        description (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        url (``str``):
            N/A

    """

    __slots__: list[str] = ["suggestion", "title", "description", "url"]

    ID = 0xe7e82e12
    QUALNAME = "types.PendingSuggestion"

    def __init__(self, *, suggestion: str, title: "raw.base.TextWithEntities", description: "raw.base.TextWithEntities", url: str) -> None:
        self.suggestion = suggestion  # string
        self.title = title  # TextWithEntities
        self.description = description  # TextWithEntities
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PendingSuggestion":
        # No flags
        
        suggestion = String.read(b)
        
        title = TLObject.read(b)
        
        description = TLObject.read(b)
        
        url = String.read(b)
        
        return PendingSuggestion(suggestion=suggestion, title=title, description=description, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.suggestion))
        
        b.write(self.title.write())
        
        b.write(self.description.write())
        
        b.write(String(self.url))
        
        return b.getvalue()
