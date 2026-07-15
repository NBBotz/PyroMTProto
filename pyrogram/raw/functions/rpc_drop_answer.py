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


class RpcDropAnswer(TLObject["raw.base.RpcDropAnswer"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``58E4A740``

    Parameters:
        req_msg_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`RpcDropAnswer <pyrogram.raw.base.RpcDropAnswer>`
    """

    __slots__: list[str] = ["req_msg_id"]

    ID = 0x58e4a740
    QUALNAME = "functions.RpcDropAnswer"

    def __init__(self, *, req_msg_id: int) -> None:
        self.req_msg_id = req_msg_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcDropAnswer":
        # No flags
        
        req_msg_id = Long.read(b)
        
        return RpcDropAnswer(req_msg_id=req_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.req_msg_id))
        
        return b.getvalue()
