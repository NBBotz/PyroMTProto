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


class GetDialogUnreadMarks(TLObject["List[raw.base.DialogPeer]"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``21202222``

    Parameters:
        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        List of :obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`
    """

    __slots__: list[str] = ["parent_peer"]

    ID = 0x21202222
    QUALNAME = "functions.messages.GetDialogUnreadMarks"

    def __init__(self, *, parent_peer: "raw.base.InputPeer" = None) -> None:
        self.parent_peer = parent_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDialogUnreadMarks":
        
        flags = Int.read(b)
        
        parent_peer = TLObject.read(b) if flags & (1 << 0) else None
        
        return GetDialogUnreadMarks(parent_peer=parent_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.parent_peer is not None else 0
        b.write(Int(flags))
        
        if self.parent_peer is not None:
            b.write(self.parent_peer.write())
        
        return b.getvalue()
