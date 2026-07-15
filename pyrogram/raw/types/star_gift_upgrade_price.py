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


class StarGiftUpgradePrice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftUpgradePrice`.

    Details:
        - Layer: ``227``
        - ID: ``99EA331D``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        upgrade_stars (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["date", "upgrade_stars"]

    ID = 0x99ea331d
    QUALNAME = "types.StarGiftUpgradePrice"

    def __init__(self, *, date: int, upgrade_stars: int) -> None:
        self.date = date  # int
        self.upgrade_stars = upgrade_stars  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUpgradePrice":
        # No flags
        
        date = Int.read(b)
        
        upgrade_stars = Long.read(b)
        
        return StarGiftUpgradePrice(date=date, upgrade_stars=upgrade_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(Long(self.upgrade_stars))
        
        return b.getvalue()
