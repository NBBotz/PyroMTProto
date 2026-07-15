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


class FinishJob(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``4F1EBF24``

    Parameters:
        job_id (``str``):
            N/A

        error (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["job_id", "error"]

    ID = 0x4f1ebf24
    QUALNAME = "functions.smsjobs.FinishJob"

    def __init__(self, *, job_id: str, error: Optional[str] = None) -> None:
        self.job_id = job_id  # string
        self.error = error  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FinishJob":
        
        flags = Int.read(b)
        
        job_id = String.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        return FinishJob(job_id=job_id, error=error)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.error is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.job_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        return b.getvalue()
