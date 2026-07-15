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


class EditBusinessChatLink(TLObject["raw.base.BusinessChatLink"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``8C3410AF``

    Parameters:
        slug (``str``):
            N/A

        link (:obj:`InputBusinessChatLink <pyrogram.raw.base.InputBusinessChatLink>`):
            N/A

    Returns:
        :obj:`BusinessChatLink <pyrogram.raw.base.BusinessChatLink>`
    """

    __slots__: list[str] = ["slug", "link"]

    ID = 0x8c3410af
    QUALNAME = "functions.account.EditBusinessChatLink"

    def __init__(self, *, slug: str, link: "raw.base.InputBusinessChatLink") -> None:
        self.slug = slug  # string
        self.link = link  # InputBusinessChatLink

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditBusinessChatLink":
        # No flags
        
        slug = String.read(b)
        
        link = TLObject.read(b)
        
        return EditBusinessChatLink(slug=slug, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        b.write(self.link.write())
        
        return b.getvalue()
