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


class JsonString(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JSONValue`.

    Details:
        - Layer: ``227``
        - ID: ``B71E767A``

    Parameters:
        value (``str``):
            N/A

    """

    __slots__: list[str] = ["value"]

    ID = 0xb71e767a
    QUALNAME = "types.JsonString"

    def __init__(self, *, value: str) -> None:
        self.value = value  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonString":
        # No flags
        
        value = String.read(b)
        
        return JsonString(value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.value))
        
        return b.getvalue()
