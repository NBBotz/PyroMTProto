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


class Ping(TLObject["raw.base.Pong"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``7ABE77EC``

    Parameters:
        ping_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`Pong <pyrogram.raw.base.Pong>`
    """

    __slots__: list[str] = ["ping_id"]

    ID = 0x7abe77ec
    QUALNAME = "functions.Ping"

    def __init__(self, *, ping_id: int) -> None:
        self.ping_id = ping_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Ping":
        # No flags
        
        ping_id = Long.read(b)
        
        return Ping(ping_id=ping_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.ping_id))
        
        return b.getvalue()
