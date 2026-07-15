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


class UpdateGroupCallEncryptedMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``C957A766``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        encrypted_message (``bytes``):
            N/A

    """

    __slots__: list[str] = ["call", "from_id", "encrypted_message"]

    ID = 0xc957a766
    QUALNAME = "types.UpdateGroupCallEncryptedMessage"

    def __init__(self, *, call: "raw.base.InputGroupCall", from_id: "raw.base.Peer", encrypted_message: bytes) -> None:
        self.call = call  # InputGroupCall
        self.from_id = from_id  # Peer
        self.encrypted_message = encrypted_message  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallEncryptedMessage":
        # No flags
        
        call = TLObject.read(b)
        
        from_id = TLObject.read(b)
        
        encrypted_message = Bytes.read(b)
        
        return UpdateGroupCallEncryptedMessage(call=call, from_id=from_id, encrypted_message=encrypted_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(self.from_id.write())
        
        b.write(Bytes(self.encrypted_message))
        
        return b.getvalue()
