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


class SentCodeTypeSmsPhrase(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``227``
        - ID: ``B37794AF``

    Parameters:
        beginning (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["beginning"]

    ID = 0xb37794af
    QUALNAME = "types.auth.SentCodeTypeSmsPhrase"

    def __init__(self, *, beginning: Optional[str] = None) -> None:
        self.beginning = beginning  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeSmsPhrase":
        
        flags = Int.read(b)
        
        beginning = String.read(b) if flags & (1 << 0) else None
        return SentCodeTypeSmsPhrase(beginning=beginning)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.beginning is not None else 0
        b.write(Int(flags))
        
        if self.beginning is not None:
            b.write(String(self.beginning))
        
        return b.getvalue()
