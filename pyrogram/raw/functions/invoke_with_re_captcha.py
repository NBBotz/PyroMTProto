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


class InvokeWithReCaptcha(TLObject["raw.base.X"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``ADBB0F94``

    Parameters:
        token (``str``):
            N/A

        query (Any function from :obj:`~pyrogram.raw.functions`):
            N/A

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: list[str] = ["token", "query"]

    ID = 0xadbb0f94
    QUALNAME = "functions.InvokeWithReCaptcha"

    def __init__(self, *, token: str, query: TLObject) -> None:
        self.token = token  # string
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithReCaptcha":
        # No flags
        
        token = String.read(b)
        
        query = TLObject.read(b)
        
        return InvokeWithReCaptcha(token=token, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.token))
        
        b.write(self.query.write())
        
        return b.getvalue()
