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


class CdnPublicKey(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.CdnPublicKey`.

    Details:
        - Layer: ``227``
        - ID: ``C982EABA``

    Parameters:
        dc_id (``int`` ``32-bit``):
            N/A

        public_key (``str``):
            N/A

    """

    __slots__: list[str] = ["dc_id", "public_key"]

    ID = 0xc982eaba
    QUALNAME = "types.CdnPublicKey"

    def __init__(self, *, dc_id: int, public_key: str) -> None:
        self.dc_id = dc_id  # int
        self.public_key = public_key  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CdnPublicKey":
        # No flags
        
        dc_id = Int.read(b)
        
        public_key = String.read(b)
        
        return CdnPublicKey(dc_id=dc_id, public_key=public_key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        b.write(String(self.public_key))
        
        return b.getvalue()
