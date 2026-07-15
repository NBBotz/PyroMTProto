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


class ExportGroupCallInvite(TLObject["raw.base.phone.ExportedGroupCallInvite"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``E6AA647F``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        can_self_unmute (``bool``, *optional*):
            N/A

    Returns:
        :obj:`phone.ExportedGroupCallInvite <pyrogram.raw.base.phone.ExportedGroupCallInvite>`
    """

    __slots__: list[str] = ["call", "can_self_unmute"]

    ID = 0xe6aa647f
    QUALNAME = "functions.phone.ExportGroupCallInvite"

    def __init__(self, *, call: "raw.base.InputGroupCall", can_self_unmute: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.can_self_unmute = can_self_unmute  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportGroupCallInvite":
        
        flags = Int.read(b)
        
        can_self_unmute = True if flags & (1 << 0) else False
        call = TLObject.read(b)
        
        return ExportGroupCallInvite(call=call, can_self_unmute=can_self_unmute)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_self_unmute else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        return b.getvalue()
