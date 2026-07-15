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


class WebPageNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPage`.

    Details:
        - Layer: ``227``
        - ID: ``7311CA11``

    Parameters:
        cached_page_views (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["cached_page_views"]

    ID = 0x7311ca11
    QUALNAME = "types.WebPageNotModified"

    def __init__(self, *, cached_page_views: Optional[int] = None) -> None:
        self.cached_page_views = cached_page_views  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageNotModified":
        
        flags = Int.read(b)
        
        cached_page_views = Int.read(b) if flags & (1 << 0) else None
        return WebPageNotModified(cached_page_views=cached_page_views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.cached_page_views is not None else 0
        b.write(Int(flags))
        
        if self.cached_page_views is not None:
            b.write(Int(self.cached_page_views))
        
        return b.getvalue()
