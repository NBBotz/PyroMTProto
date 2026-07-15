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


class StarGiftAuctionAcquiredGifts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftAuctionAcquiredGifts`.

    Details:
        - Layer: ``227``
        - ID: ``7D5BD1F0``

    Parameters:
        gifts (List of :obj:`StarGiftAuctionAcquiredGift <pyrogram.raw.base.StarGiftAuctionAcquiredGift>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftAuctionAcquiredGifts
    """

    __slots__: list[str] = ["gifts", "users", "chats"]

    ID = 0x7d5bd1f0
    QUALNAME = "types.payments.StarGiftAuctionAcquiredGifts"

    def __init__(self, *, gifts: list["raw.base.StarGiftAuctionAcquiredGift"], users: list["raw.base.User"], chats: list["raw.base.Chat"]) -> None:
        self.gifts = gifts  # Vector<StarGiftAuctionAcquiredGift>
        self.users = users  # Vector<User>
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionAcquiredGifts":
        # No flags
        
        gifts = TLObject.read(b)
        
        users = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        return StarGiftAuctionAcquiredGifts(gifts=gifts, users=users, chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.gifts))
        
        b.write(Vector(self.users))
        
        b.write(Vector(self.chats))
        
        return b.getvalue()
