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


class PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PasswordKdfAlgo`.

    Details:
        - Layer: ``227``
        - ID: ``3A912D4A``

    Parameters:
        salt1 (``bytes``):
            N/A

        salt2 (``bytes``):
            N/A

        g (``int`` ``32-bit``):
            N/A

        p (``bytes``):
            N/A

    """

    __slots__: list[str] = ["salt1", "salt2", "g", "p"]

    ID = 0x3a912d4a
    QUALNAME = "types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"

    def __init__(self, *, salt1: bytes, salt2: bytes, g: int, p: bytes) -> None:
        self.salt1 = salt1  # bytes
        self.salt2 = salt2  # bytes
        self.g = g  # int
        self.p = p  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow":
        # No flags
        
        salt1 = Bytes.read(b)
        
        salt2 = Bytes.read(b)
        
        g = Int.read(b)
        
        p = Bytes.read(b)
        
        return PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(salt1=salt1, salt2=salt2, g=g, p=p)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.salt1))
        
        b.write(Bytes(self.salt2))
        
        b.write(Int(self.g))
        
        b.write(Bytes(self.p))
        
        return b.getvalue()
