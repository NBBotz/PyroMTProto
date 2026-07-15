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


class PageBlockAnchor(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``227``
        - ID: ``CE0D37B0``

    Parameters:
        name (``str``):
            N/A

    """

    __slots__: list[str] = ["name"]

    ID = 0xce0d37b0
    QUALNAME = "types.PageBlockAnchor"

    def __init__(self, *, name: str) -> None:
        self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockAnchor":
        # No flags
        
        name = String.read(b)
        
        return PageBlockAnchor(name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.name))
        
        return b.getvalue()
