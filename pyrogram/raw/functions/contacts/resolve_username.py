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


class ResolveUsername(TLObject["raw.base.contacts.ResolvedPeer"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``725AFBBC``

    Parameters:
        username (``str``):
            N/A

        referer (``str``, *optional*):
            N/A

    Returns:
        :obj:`contacts.ResolvedPeer <pyrogram.raw.base.contacts.ResolvedPeer>`
    """

    __slots__: list[str] = ["username", "referer"]

    ID = 0x725afbbc
    QUALNAME = "functions.contacts.ResolveUsername"

    def __init__(self, *, username: str, referer: Optional[str] = None) -> None:
        self.username = username  # string
        self.referer = referer  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveUsername":
        
        flags = Int.read(b)
        
        username = String.read(b)
        
        referer = String.read(b) if flags & (1 << 0) else None
        return ResolveUsername(username=username, referer=referer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.referer is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.username))
        
        if self.referer is not None:
            b.write(String(self.referer))
        
        return b.getvalue()
