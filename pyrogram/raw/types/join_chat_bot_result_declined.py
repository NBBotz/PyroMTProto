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


class JoinChatBotResultDeclined(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JoinChatBotResult`.

    Details:
        - Layer: ``227``
        - ID: ``EFA0194``

    Parameters:
        No parameters required.

    """

    __slots__: list[str] = []

    ID = 0xefa0194
    QUALNAME = "types.JoinChatBotResultDeclined"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinChatBotResultDeclined":
        # No flags
        
        return JoinChatBotResultDeclined()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
