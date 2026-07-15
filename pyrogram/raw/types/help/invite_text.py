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


class InviteText(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.InviteText`.

    Details:
        - Layer: ``227``
        - ID: ``18CB9F78``

    Parameters:
        message (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetInviteText
    """

    __slots__: list[str] = ["message"]

    ID = 0x18cb9f78
    QUALNAME = "types.help.InviteText"

    def __init__(self, *, message: str) -> None:
        self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteText":
        # No flags
        
        message = String.read(b)
        
        return InviteText(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.message))
        
        return b.getvalue()
