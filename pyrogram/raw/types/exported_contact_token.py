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


class ExportedContactToken(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ExportedContactToken`.

    Details:
        - Layer: ``227``
        - ID: ``41BF109B``

    Parameters:
        url (``str``):
            N/A

        expires (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ExportContactToken
    """

    __slots__: list[str] = ["url", "expires"]

    ID = 0x41bf109b
    QUALNAME = "types.ExportedContactToken"

    def __init__(self, *, url: str, expires: int) -> None:
        self.url = url  # string
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedContactToken":
        # No flags
        
        url = String.read(b)
        
        expires = Int.read(b)
        
        return ExportedContactToken(url=url, expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Int(self.expires))
        
        return b.getvalue()
