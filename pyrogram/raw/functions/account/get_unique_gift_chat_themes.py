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


class GetUniqueGiftChatThemes(TLObject["raw.base.account.ChatThemes"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``E42CE9C9``

    Parameters:
        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`account.ChatThemes <pyrogram.raw.base.account.ChatThemes>`
    """

    __slots__: list[str] = ["offset", "limit", "hash"]

    ID = 0xe42ce9c9
    QUALNAME = "functions.account.GetUniqueGiftChatThemes"

    def __init__(self, *, offset: str, limit: int, hash: int) -> None:
        self.offset = offset  # string
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUniqueGiftChatThemes":
        # No flags
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetUniqueGiftChatThemes(offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
