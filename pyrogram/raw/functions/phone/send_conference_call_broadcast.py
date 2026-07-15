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


class SendConferenceCallBroadcast(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``C6701900``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        block (``bytes``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = ["call", "block"]

    ID = 0xc6701900
    QUALNAME = "functions.phone.SendConferenceCallBroadcast"

    def __init__(self, *, call: "raw.base.InputGroupCall", block: bytes) -> None:
        self.call = call  # InputGroupCall
        self.block = block  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendConferenceCallBroadcast":
        # No flags
        
        call = TLObject.read(b)
        
        block = Bytes.read(b)
        
        return SendConferenceCallBroadcast(call=call, block=block)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Bytes(self.block))
        
        return b.getvalue()
