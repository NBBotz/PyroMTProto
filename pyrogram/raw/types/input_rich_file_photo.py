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


class InputRichFilePhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputRichFile`.

    Details:
        - Layer: ``227``
        - ID: ``9B00622B``

    Parameters:
        id (``str``):
            N/A

        photo (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            N/A

    """

    __slots__: list[str] = ["id", "photo"]

    ID = 0x9b00622b
    QUALNAME = "types.InputRichFilePhoto"

    def __init__(self, *, id: str, photo: "raw.base.InputPhoto") -> None:
        self.id = id  # string
        self.photo = photo  # InputPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputRichFilePhoto":
        # No flags
        
        id = String.read(b)
        
        photo = TLObject.read(b)
        
        return InputRichFilePhoto(id=id, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(self.photo.write())
        
        return b.getvalue()
