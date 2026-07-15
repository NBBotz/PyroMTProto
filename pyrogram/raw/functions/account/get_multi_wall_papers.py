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


class GetMultiWallPapers(TLObject["List[raw.base.WallPaper]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``65AD71DC``

    Parameters:
        wallpapers (List of :obj:`InputWallPaper <pyrogram.raw.base.InputWallPaper>`):
            N/A

    Returns:
        List of :obj:`WallPaper <pyrogram.raw.base.WallPaper>`
    """

    __slots__: list[str] = ["wallpapers"]

    ID = 0x65ad71dc
    QUALNAME = "functions.account.GetMultiWallPapers"

    def __init__(self, *, wallpapers: list["raw.base.InputWallPaper"]) -> None:
        self.wallpapers = wallpapers  # Vector<InputWallPaper>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMultiWallPapers":
        # No flags
        
        wallpapers = TLObject.read(b)
        
        return GetMultiWallPapers(wallpapers=wallpapers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.wallpapers))
        
        return b.getvalue()
