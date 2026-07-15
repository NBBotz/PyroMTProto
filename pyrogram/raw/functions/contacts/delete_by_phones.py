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


class DeleteByPhones(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``1013FD9E``

    Parameters:
        phones (List of ``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["phones"]

    ID = 0x1013fd9e
    QUALNAME = "functions.contacts.DeleteByPhones"

    def __init__(self, *, phones: list[str]) -> None:
        self.phones = phones  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteByPhones":
        # No flags
        
        phones = TLObject.read(b, String)
        
        return DeleteByPhones(phones=phones)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.phones, String))
        
        return b.getvalue()
