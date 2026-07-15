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


class RpcAnswerDropped(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RpcDropAnswer`.

    Details:
        - Layer: ``227``
        - ID: ``A43AD8B7``

    Parameters:
        msg_id (``int`` ``64-bit``):
            N/A

        seq_no (``int`` ``32-bit``):
            N/A

        bytes (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            RpcDropAnswer
    """

    __slots__: list[str] = ["msg_id", "seq_no", "bytes"]

    ID = 0xa43ad8b7
    QUALNAME = "types.RpcAnswerDropped"

    def __init__(self, *, msg_id: int, seq_no: int, bytes: int) -> None:
        self.msg_id = msg_id  # long
        self.seq_no = seq_no  # int
        self.bytes = bytes  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcAnswerDropped":
        # No flags
        
        msg_id = Long.read(b)
        
        seq_no = Int.read(b)
        
        bytes = Int.read(b)
        
        return RpcAnswerDropped(msg_id=msg_id, seq_no=seq_no, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.msg_id))
        
        b.write(Int(self.seq_no))
        
        b.write(Int(self.bytes))
        
        return b.getvalue()
