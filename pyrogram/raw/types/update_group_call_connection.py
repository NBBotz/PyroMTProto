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


class UpdateGroupCallConnection(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``B783982``

    Parameters:
        params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        presentation (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["params", "presentation"]

    ID = 0xb783982
    QUALNAME = "types.UpdateGroupCallConnection"

    def __init__(self, *, params: "raw.base.DataJSON", presentation: Optional[bool] = None) -> None:
        self.params = params  # DataJSON
        self.presentation = presentation  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallConnection":
        
        flags = Int.read(b)
        
        presentation = True if flags & (1 << 0) else False
        params = TLObject.read(b)
        
        return UpdateGroupCallConnection(params=params, presentation=presentation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.presentation else 0
        b.write(Int(flags))
        
        b.write(self.params.write())
        
        return b.getvalue()
