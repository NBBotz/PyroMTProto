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


class GetDialogFilters(TLObject["raw.base.messages.DialogFilters"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``EFD48C89``

    Parameters:
        No parameters required.

    Returns:
        :obj:`messages.DialogFilters <pyrogram.raw.base.messages.DialogFilters>`
    """

    __slots__: list[str] = []

    ID = 0xefd48c89
    QUALNAME = "functions.messages.GetDialogFilters"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDialogFilters":
        # No flags
        
        return GetDialogFilters()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
