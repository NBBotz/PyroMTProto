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


class UpdateBotWebhookJSONQuery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``9B9240A6``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        timeout (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["query_id", "data", "timeout"]

    ID = 0x9b9240a6
    QUALNAME = "types.UpdateBotWebhookJSONQuery"

    def __init__(self, *, query_id: int, data: "raw.base.DataJSON", timeout: int) -> None:
        self.query_id = query_id  # long
        self.data = data  # DataJSON
        self.timeout = timeout  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotWebhookJSONQuery":
        # No flags
        
        query_id = Long.read(b)
        
        data = TLObject.read(b)
        
        timeout = Int.read(b)
        
        return UpdateBotWebhookJSONQuery(query_id=query_id, data=data, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(self.data.write())
        
        b.write(Int(self.timeout))
        
        return b.getvalue()
