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


class InputRichMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputRichMessage`.

    Details:
        - Layer: ``227``
        - ID: ``E4C449FC``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        rtl (``bool``, *optional*):
            N/A

        noautolink (``bool``, *optional*):
            N/A

        photos (List of :obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`, *optional*):
            N/A

        documents (List of :obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "rtl", "noautolink", "photos", "documents", "users"]

    ID = 0xe4c449fc
    QUALNAME = "types.InputRichMessage"

    def __init__(self, *, blocks: list["raw.base.PageBlock"], rtl: Optional[bool] = None, noautolink: Optional[bool] = None, photos: Optional[list["raw.base.InputPhoto"]] = None, documents: Optional[list["raw.base.InputDocument"]] = None, users: Optional[list["raw.base.InputUser"]] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.rtl = rtl  # flags.0?true
        self.noautolink = noautolink  # flags.1?true
        self.photos = photos  # flags.2?Vector<InputPhoto>
        self.documents = documents  # flags.3?Vector<InputDocument>
        self.users = users  # flags.4?Vector<InputUser>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputRichMessage":
        
        flags = Int.read(b)
        
        rtl = True if flags & (1 << 0) else False
        noautolink = True if flags & (1 << 1) else False
        blocks = TLObject.read(b)
        
        photos = TLObject.read(b) if flags & (1 << 2) else []
        
        documents = TLObject.read(b) if flags & (1 << 3) else []
        
        users = TLObject.read(b) if flags & (1 << 4) else []
        
        return InputRichMessage(blocks=blocks, rtl=rtl, noautolink=noautolink, photos=photos, documents=documents, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rtl else 0
        flags |= (1 << 1) if self.noautolink else 0
        flags |= (1 << 2) if self.photos else 0
        flags |= (1 << 3) if self.documents else 0
        flags |= (1 << 4) if self.users else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        if self.photos is not None:
            b.write(Vector(self.photos))
        
        if self.documents is not None:
            b.write(Vector(self.documents))
        
        if self.users is not None:
            b.write(Vector(self.users))
        
        return b.getvalue()
