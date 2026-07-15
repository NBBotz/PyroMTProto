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


class CheckHistoryImport(TLObject["raw.base.messages.HistoryImportParsed"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``43FE19F3``

    Parameters:
        import_head (``str``):
            N/A

    Returns:
        :obj:`messages.HistoryImportParsed <pyrogram.raw.base.messages.HistoryImportParsed>`
    """

    __slots__: list[str] = ["import_head"]

    ID = 0x43fe19f3
    QUALNAME = "functions.messages.CheckHistoryImport"

    def __init__(self, *, import_head: str) -> None:
        self.import_head = import_head  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckHistoryImport":
        # No flags
        
        import_head = String.read(b)
        
        return CheckHistoryImport(import_head=import_head)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.import_head))
        
        return b.getvalue()
