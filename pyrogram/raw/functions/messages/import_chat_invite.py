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


class ImportChatInvite(TLObject["raw.base.messages.ChatInviteJoinResult"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``DE91436E``

    Parameters:
        hash (``str``):
            N/A

    Returns:
        :obj:`messages.ChatInviteJoinResult <pyrogram.raw.base.messages.ChatInviteJoinResult>`
    """

    __slots__: list[str] = ["hash"]

    ID = 0xde91436e
    QUALNAME = "functions.messages.ImportChatInvite"

    def __init__(self, *, hash: str) -> None:
        self.hash = hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportChatInvite":
        # No flags
        
        hash = String.read(b)
        
        return ImportChatInvite(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.hash))
        
        return b.getvalue()
