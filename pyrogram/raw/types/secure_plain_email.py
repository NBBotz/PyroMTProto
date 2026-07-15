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


class SecurePlainEmail(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecurePlainData`.

    Details:
        - Layer: ``227``
        - ID: ``21EC5A5F``

    Parameters:
        email (``str``):
            N/A

    """

    __slots__: list[str] = ["email"]

    ID = 0x21ec5a5f
    QUALNAME = "types.SecurePlainEmail"

    def __init__(self, *, email: str) -> None:
        self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePlainEmail":
        # No flags
        
        email = String.read(b)
        
        return SecurePlainEmail(email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email))
        
        return b.getvalue()
