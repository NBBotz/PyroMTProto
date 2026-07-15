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


class InputClientProxy(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputClientProxy`.

    Details:
        - Layer: ``227``
        - ID: ``75588B3F``

    Parameters:
        address (``str``):
            N/A

        port (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["address", "port"]

    ID = 0x75588b3f
    QUALNAME = "types.InputClientProxy"

    def __init__(self, *, address: str, port: int) -> None:
        self.address = address  # string
        self.port = port  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputClientProxy":
        # No flags
        
        address = String.read(b)
        
        port = Int.read(b)
        
        return InputClientProxy(address=address, port=port)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.address))
        
        b.write(Int(self.port))
        
        return b.getvalue()
