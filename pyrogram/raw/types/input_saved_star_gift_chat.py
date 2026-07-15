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


class InputSavedStarGiftChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputSavedStarGift`.

    Details:
        - Layer: ``227``
        - ID: ``F101AA7F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        saved_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["peer", "saved_id"]

    ID = 0xf101aa7f
    QUALNAME = "types.InputSavedStarGiftChat"

    def __init__(self, *, peer: "raw.base.InputPeer", saved_id: int) -> None:
        self.peer = peer  # InputPeer
        self.saved_id = saved_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputSavedStarGiftChat":
        # No flags
        
        peer = TLObject.read(b)
        
        saved_id = Long.read(b)
        
        return InputSavedStarGiftChat(peer=peer, saved_id=saved_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.saved_id))
        
        return b.getvalue()
