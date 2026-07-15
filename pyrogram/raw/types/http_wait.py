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


class HttpWait(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.HttpWait`.

    Details:
        - Layer: ``227``
        - ID: ``9299359F``

    Parameters:
        max_delay (``int`` ``32-bit``):
            N/A

        wait_after (``int`` ``32-bit``):
            N/A

        max_wait (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["max_delay", "wait_after", "max_wait"]

    ID = 0x9299359f
    QUALNAME = "types.HttpWait"

    def __init__(self, *, max_delay: int, wait_after: int, max_wait: int) -> None:
        self.max_delay = max_delay  # int
        self.wait_after = wait_after  # int
        self.max_wait = max_wait  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HttpWait":
        # No flags
        
        max_delay = Int.read(b)
        
        wait_after = Int.read(b)
        
        max_wait = Int.read(b)
        
        return HttpWait(max_delay=max_delay, wait_after=wait_after, max_wait=max_wait)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.max_delay))
        
        b.write(Int(self.wait_after))
        
        b.write(Int(self.max_wait))
        
        return b.getvalue()
