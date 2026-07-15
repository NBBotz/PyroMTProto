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


class InputMediaPaidMedia(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``227``
        - ID: ``C4103386``

    Parameters:
        stars_amount (``int`` ``64-bit``):
            N/A

        extended_media (List of :obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

        payload (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["stars_amount", "extended_media", "payload"]

    ID = 0xc4103386
    QUALNAME = "types.InputMediaPaidMedia"

    def __init__(self, *, stars_amount: int, extended_media: list["raw.base.InputMedia"], payload: Optional[str] = None) -> None:
        self.stars_amount = stars_amount  # long
        self.extended_media = extended_media  # Vector<InputMedia>
        self.payload = payload  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPaidMedia":
        
        flags = Int.read(b)
        
        stars_amount = Long.read(b)
        
        extended_media = TLObject.read(b)
        
        payload = String.read(b) if flags & (1 << 0) else None
        return InputMediaPaidMedia(stars_amount=stars_amount, extended_media=extended_media, payload=payload)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.payload is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.stars_amount))
        
        b.write(Vector(self.extended_media))
        
        if self.payload is not None:
            b.write(String(self.payload))
        
        return b.getvalue()
