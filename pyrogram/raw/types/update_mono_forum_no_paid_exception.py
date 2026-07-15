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


class UpdateMonoForumNoPaidException(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``9F812B08``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        exception (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["channel_id", "saved_peer_id", "exception"]

    ID = 0x9f812b08
    QUALNAME = "types.UpdateMonoForumNoPaidException"

    def __init__(self, *, channel_id: int, saved_peer_id: "raw.base.Peer", exception: Optional[bool] = None) -> None:
        self.channel_id = channel_id  # long
        self.saved_peer_id = saved_peer_id  # Peer
        self.exception = exception  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMonoForumNoPaidException":
        
        flags = Int.read(b)
        
        exception = True if flags & (1 << 0) else False
        channel_id = Long.read(b)
        
        saved_peer_id = TLObject.read(b)
        
        return UpdateMonoForumNoPaidException(channel_id=channel_id, saved_peer_id=saved_peer_id, exception=exception)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exception else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        b.write(self.saved_peer_id.write())
        
        return b.getvalue()
