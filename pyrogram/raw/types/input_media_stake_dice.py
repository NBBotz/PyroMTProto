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


class InputMediaStakeDice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``227``
        - ID: ``F3A9244A``

    Parameters:
        game_hash (``str``):
            N/A

        ton_amount (``int`` ``64-bit``):
            N/A

        client_seed (``bytes``):
            N/A

    """

    __slots__: list[str] = ["game_hash", "ton_amount", "client_seed"]

    ID = 0xf3a9244a
    QUALNAME = "types.InputMediaStakeDice"

    def __init__(self, *, game_hash: str, ton_amount: int, client_seed: bytes) -> None:
        self.game_hash = game_hash  # string
        self.ton_amount = ton_amount  # long
        self.client_seed = client_seed  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaStakeDice":
        # No flags
        
        game_hash = String.read(b)
        
        ton_amount = Long.read(b)
        
        client_seed = Bytes.read(b)
        
        return InputMediaStakeDice(game_hash=game_hash, ton_amount=ton_amount, client_seed=client_seed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.game_hash))
        
        b.write(Long(self.ton_amount))
        
        b.write(Bytes(self.client_seed))
        
        return b.getvalue()
