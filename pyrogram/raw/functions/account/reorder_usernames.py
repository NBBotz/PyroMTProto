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


class ReorderUsernames(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``EF500EAB``

    Parameters:
        order (List of ``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["order"]

    ID = 0xef500eab
    QUALNAME = "functions.account.ReorderUsernames"

    def __init__(self, *, order: list[str]) -> None:
        self.order = order  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderUsernames":
        # No flags
        
        order = TLObject.read(b, String)
        
        return ReorderUsernames(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.order, String))
        
        return b.getvalue()
