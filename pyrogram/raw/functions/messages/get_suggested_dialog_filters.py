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


class GetSuggestedDialogFilters(TLObject["List[raw.base.DialogFilterSuggested]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``A29CD42C``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`DialogFilterSuggested <pyrogram.raw.base.DialogFilterSuggested>`
    """

    __slots__: list[str] = []

    ID = 0xa29cd42c
    QUALNAME = "functions.messages.GetSuggestedDialogFilters"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSuggestedDialogFilters":
        # No flags
        
        return GetSuggestedDialogFilters()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
