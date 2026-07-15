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


class InputInvoiceStarGiftPrepaidUpgrade(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``227``
        - ID: ``9A0B48B8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        hash (``str``):
            N/A

    """

    __slots__: list[str] = ["peer", "hash"]

    ID = 0x9a0b48b8
    QUALNAME = "types.InputInvoiceStarGiftPrepaidUpgrade"

    def __init__(self, *, peer: "raw.base.InputPeer", hash: str) -> None:
        self.peer = peer  # InputPeer
        self.hash = hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftPrepaidUpgrade":
        # No flags
        
        peer = TLObject.read(b)
        
        hash = String.read(b)
        
        return InputInvoiceStarGiftPrepaidUpgrade(peer=peer, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(String(self.hash))
        
        return b.getvalue()
