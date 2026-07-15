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


class MessageActionChangeCreator(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``E188503B``

    Parameters:
        new_creator_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["new_creator_id"]

    ID = 0xe188503b
    QUALNAME = "types.MessageActionChangeCreator"

    def __init__(self, *, new_creator_id: int) -> None:
        self.new_creator_id = new_creator_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChangeCreator":
        # No flags
        
        new_creator_id = Long.read(b)
        
        return MessageActionChangeCreator(new_creator_id=new_creator_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.new_creator_id))
        
        return b.getvalue()
