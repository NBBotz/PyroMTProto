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


class EmojiGameOutcome(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.EmojiGameOutcome`.

    Details:
        - Layer: ``227``
        - ID: ``DA2AD647``

    Parameters:
        seed (``bytes``):
            N/A

        stake_ton_amount (``int`` ``64-bit``):
            N/A

        ton_amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["seed", "stake_ton_amount", "ton_amount"]

    ID = 0xda2ad647
    QUALNAME = "types.messages.EmojiGameOutcome"

    def __init__(self, *, seed: bytes, stake_ton_amount: int, ton_amount: int) -> None:
        self.seed = seed  # bytes
        self.stake_ton_amount = stake_ton_amount  # long
        self.ton_amount = ton_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGameOutcome":
        # No flags
        
        seed = Bytes.read(b)
        
        stake_ton_amount = Long.read(b)
        
        ton_amount = Long.read(b)
        
        return EmojiGameOutcome(seed=seed, stake_ton_amount=stake_ton_amount, ton_amount=ton_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.seed))
        
        b.write(Long(self.stake_ton_amount))
        
        b.write(Long(self.ton_amount))
        
        return b.getvalue()
