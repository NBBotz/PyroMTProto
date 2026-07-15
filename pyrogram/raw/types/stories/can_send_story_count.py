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


class CanSendStoryCount(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.CanSendStoryCount`.

    Details:
        - Layer: ``227``
        - ID: ``C387C04E``

    Parameters:
        count_remains (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.CanSendStory
    """

    __slots__: list[str] = ["count_remains"]

    ID = 0xc387c04e
    QUALNAME = "types.stories.CanSendStoryCount"

    def __init__(self, *, count_remains: int) -> None:
        self.count_remains = count_remains  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CanSendStoryCount":
        # No flags
        
        count_remains = Int.read(b)
        
        return CanSendStoryCount(count_remains=count_remains)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count_remains))
        
        return b.getvalue()
