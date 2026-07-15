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


class PageListItemText(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageListItem`.

    Details:
        - Layer: ``227``
        - ID: ``2F58683C``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        checkbox (``bool``, *optional*):
            N/A

        checked (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["text", "checkbox", "checked"]

    ID = 0x2f58683c
    QUALNAME = "types.PageListItemText"

    def __init__(self, *, text: "raw.base.RichText", checkbox: Optional[bool] = None, checked: Optional[bool] = None) -> None:
        self.text = text  # RichText
        self.checkbox = checkbox  # flags.0?true
        self.checked = checked  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListItemText":
        
        flags = Int.read(b)
        
        checkbox = True if flags & (1 << 0) else False
        checked = True if flags & (1 << 1) else False
        text = TLObject.read(b)
        
        return PageListItemText(text=text, checkbox=checkbox, checked=checked)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.checkbox else 0
        flags |= (1 << 1) if self.checked else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        return b.getvalue()
