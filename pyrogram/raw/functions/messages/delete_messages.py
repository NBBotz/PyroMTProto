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


class DeleteMessages(TLObject["raw.base.messages.AffectedMessages"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``E58E95D2``

    Parameters:
        id (List of ``int`` ``32-bit``):
            N/A

        revoke (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.AffectedMessages <pyrogram.raw.base.messages.AffectedMessages>`
    """

    __slots__: list[str] = ["id", "revoke"]

    ID = 0xe58e95d2
    QUALNAME = "functions.messages.DeleteMessages"

    def __init__(self, *, id: list[int], revoke: Optional[bool] = None) -> None:
        self.id = id  # Vector<int>
        self.revoke = revoke  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteMessages":
        
        flags = Int.read(b)
        
        revoke = True if flags & (1 << 0) else False
        id = TLObject.read(b, Int)
        
        return DeleteMessages(id=id, revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke else 0
        b.write(Int(flags))
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()
