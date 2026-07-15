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


class EditConnectedStarRefBot(TLObject["raw.base.payments.ConnectedStarRefBots"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``E4FCA4A3``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        link (``str``):
            N/A

        revoked (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.ConnectedStarRefBots <pyrogram.raw.base.payments.ConnectedStarRefBots>`
    """

    __slots__: list[str] = ["peer", "link", "revoked"]

    ID = 0xe4fca4a3
    QUALNAME = "functions.payments.EditConnectedStarRefBot"

    def __init__(self, *, peer: "raw.base.InputPeer", link: str, revoked: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.link = link  # string
        self.revoked = revoked  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditConnectedStarRefBot":
        
        flags = Int.read(b)
        
        revoked = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        link = String.read(b)
        
        return EditConnectedStarRefBot(peer=peer, link=link, revoked=revoked)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoked else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.link))
        
        return b.getvalue()
