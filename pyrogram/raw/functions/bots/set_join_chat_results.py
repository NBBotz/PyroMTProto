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


class SetJoinChatResults(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``E71A4810``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        result (:obj:`JoinChatBotResult <pyrogram.raw.base.JoinChatBotResult>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["query_id", "result"]

    ID = 0xe71a4810
    QUALNAME = "functions.bots.SetJoinChatResults"

    def __init__(self, *, query_id: int, result: "raw.base.JoinChatBotResult") -> None:
        self.query_id = query_id  # long
        self.result = result  # JoinChatBotResult

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetJoinChatResults":
        # No flags
        
        query_id = Long.read(b)
        
        result = TLObject.read(b)
        
        return SetJoinChatResults(query_id=query_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(self.result.write())
        
        return b.getvalue()
