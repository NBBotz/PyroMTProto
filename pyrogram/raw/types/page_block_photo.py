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


class PageBlockPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``227``
        - ID: ``1759C560``

    Parameters:
        photo_id (``int`` ``64-bit``):
            N/A

        caption (:obj:`PageCaption <pyrogram.raw.base.PageCaption>`):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        webpage_id (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["photo_id", "caption", "spoiler", "url", "webpage_id"]

    ID = 0x1759c560
    QUALNAME = "types.PageBlockPhoto"

    def __init__(self, *, photo_id: int, caption: "raw.base.PageCaption", spoiler: Optional[bool] = None, url: Optional[str] = None, webpage_id: Optional[int] = None) -> None:
        self.photo_id = photo_id  # long
        self.caption = caption  # PageCaption
        self.spoiler = spoiler  # flags.1?true
        self.url = url  # flags.0?string
        self.webpage_id = webpage_id  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPhoto":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 1) else False
        photo_id = Long.read(b)
        
        caption = TLObject.read(b)
        
        url = String.read(b) if flags & (1 << 0) else None
        webpage_id = Long.read(b) if flags & (1 << 0) else None
        return PageBlockPhoto(photo_id=photo_id, caption=caption, spoiler=spoiler, url=url, webpage_id=webpage_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.spoiler else 0
        flags |= (1 << 0) if self.url is not None else 0
        flags |= (1 << 0) if self.webpage_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.photo_id))
        
        b.write(self.caption.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.webpage_id is not None:
            b.write(Long(self.webpage_id))
        
        return b.getvalue()
