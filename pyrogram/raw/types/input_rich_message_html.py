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


class InputRichMessageHTML(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputRichMessage`.

    Details:
        - Layer: ``227``
        - ID: ``DACB836A``

    Parameters:
        html (``str``):
            N/A

        rtl (``bool``, *optional*):
            N/A

        noautolink (``bool``, *optional*):
            N/A

        files (List of :obj:`InputRichFile <pyrogram.raw.base.InputRichFile>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["html", "rtl", "noautolink", "files"]

    ID = 0xdacb836a
    QUALNAME = "types.InputRichMessageHTML"

    def __init__(self, *, html: str, rtl: Optional[bool] = None, noautolink: Optional[bool] = None, files: Optional[list["raw.base.InputRichFile"]] = None) -> None:
        self.html = html  # string
        self.rtl = rtl  # flags.0?true
        self.noautolink = noautolink  # flags.1?true
        self.files = files  # flags.2?Vector<InputRichFile>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputRichMessageHTML":
        
        flags = Int.read(b)
        
        rtl = True if flags & (1 << 0) else False
        noautolink = True if flags & (1 << 1) else False
        html = String.read(b)
        
        files = TLObject.read(b) if flags & (1 << 2) else []
        
        return InputRichMessageHTML(html=html, rtl=rtl, noautolink=noautolink, files=files)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rtl else 0
        flags |= (1 << 1) if self.noautolink else 0
        flags |= (1 << 2) if self.files else 0
        b.write(Int(flags))
        
        b.write(String(self.html))
        
        if self.files is not None:
            b.write(Vector(self.files))
        
        return b.getvalue()
