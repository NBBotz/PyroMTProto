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


class UpdateBotBusinessConnect(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``8AE5C97A``

    Parameters:
        connection (:obj:`BotBusinessConnection <pyrogram.raw.base.BotBusinessConnection>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["connection", "qts"]

    ID = 0x8ae5c97a
    QUALNAME = "types.UpdateBotBusinessConnect"

    def __init__(self, *, connection: "raw.base.BotBusinessConnection", qts: int) -> None:
        self.connection = connection  # BotBusinessConnection
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotBusinessConnect":
        # No flags
        
        connection = TLObject.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotBusinessConnect(connection=connection, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.connection.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
