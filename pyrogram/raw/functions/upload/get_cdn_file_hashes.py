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


class GetCdnFileHashes(TLObject["List[raw.base.FileHash]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``91DC3F31``

    Parameters:
        file_token (``bytes``):
            N/A

        offset (``int`` ``64-bit``):
            N/A

    Returns:
        List of :obj:`FileHash <pyrogram.raw.base.FileHash>`
    """

    __slots__: list[str] = ["file_token", "offset"]

    ID = 0x91dc3f31
    QUALNAME = "functions.upload.GetCdnFileHashes"

    def __init__(self, *, file_token: bytes, offset: int) -> None:
        self.file_token = file_token  # bytes
        self.offset = offset  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCdnFileHashes":
        # No flags
        
        file_token = Bytes.read(b)
        
        offset = Long.read(b)
        
        return GetCdnFileHashes(file_token=file_token, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.file_token))
        
        b.write(Long(self.offset))
        
        return b.getvalue()
