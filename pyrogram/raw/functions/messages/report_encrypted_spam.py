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


class ReportEncryptedSpam(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``4B0C8C0F``

    Parameters:
        peer (:obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["peer"]

    ID = 0x4b0c8c0f
    QUALNAME = "functions.messages.ReportEncryptedSpam"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat") -> None:
        self.peer = peer  # InputEncryptedChat

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportEncryptedSpam":
        # No flags
        
        peer = TLObject.read(b)
        
        return ReportEncryptedSpam(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()
