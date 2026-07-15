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


class GetAllSecureValues(TLObject["List[raw.base.SecureValue]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``B288BC7D``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`SecureValue <pyrogram.raw.base.SecureValue>`
    """

    __slots__: list[str] = []

    ID = 0xb288bc7d
    QUALNAME = "functions.account.GetAllSecureValues"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAllSecureValues":
        # No flags
        
        return GetAllSecureValues()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
