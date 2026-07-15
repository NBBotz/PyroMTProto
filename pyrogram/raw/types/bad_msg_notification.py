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


class BadMsgNotification(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BadMsgNotification`.

    Details:
        - Layer: ``227``
        - ID: ``A7EFF811``

    Parameters:
        bad_msg_id (``int`` ``64-bit``):
            N/A

        bad_msg_seqno (``int`` ``32-bit``):
            N/A

        error_code (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["bad_msg_id", "bad_msg_seqno", "error_code"]

    ID = 0xa7eff811
    QUALNAME = "types.BadMsgNotification"

    def __init__(self, *, bad_msg_id: int, bad_msg_seqno: int, error_code: int) -> None:
        self.bad_msg_id = bad_msg_id  # long
        self.bad_msg_seqno = bad_msg_seqno  # int
        self.error_code = error_code  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BadMsgNotification":
        # No flags
        
        bad_msg_id = Long.read(b)
        
        bad_msg_seqno = Int.read(b)
        
        error_code = Int.read(b)
        
        return BadMsgNotification(bad_msg_id=bad_msg_id, bad_msg_seqno=bad_msg_seqno, error_code=error_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bad_msg_id))
        
        b.write(Int(self.bad_msg_seqno))
        
        b.write(Int(self.error_code))
        
        return b.getvalue()
