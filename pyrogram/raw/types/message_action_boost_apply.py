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


class MessageActionBoostApply(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``227``
        - ID: ``CC02AA6D``

    Parameters:
        boosts (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["boosts"]

    ID = 0xcc02aa6d
    QUALNAME = "types.MessageActionBoostApply"

    def __init__(self, *, boosts: int) -> None:
        self.boosts = boosts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionBoostApply":
        # No flags
        
        boosts = Int.read(b)
        
        return MessageActionBoostApply(boosts=boosts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.boosts))
        
        return b.getvalue()
