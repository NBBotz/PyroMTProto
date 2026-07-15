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


class JsonObject(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JSONValue`.

    Details:
        - Layer: ``227``
        - ID: ``99C1D49D``

    Parameters:
        value (List of :obj:`JSONObjectValue <pyrogram.raw.base.JSONObjectValue>`):
            N/A

    """

    __slots__: list[str] = ["value"]

    ID = 0x99c1d49d
    QUALNAME = "types.JsonObject"

    def __init__(self, *, value: list["raw.base.JSONObjectValue"]) -> None:
        self.value = value  # Vector<JSONObjectValue>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonObject":
        # No flags
        
        value = TLObject.read(b)
        
        return JsonObject(value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.value))
        
        return b.getvalue()
