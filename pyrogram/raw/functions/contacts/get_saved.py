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


class GetSaved(TLObject["List[raw.base.SavedContact]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``82F1E39F``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`SavedContact <pyrogram.raw.base.SavedContact>`
    """

    __slots__: list[str] = []

    ID = 0x82f1e39f
    QUALNAME = "functions.contacts.GetSaved"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSaved":
        # No flags
        
        return GetSaved()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
