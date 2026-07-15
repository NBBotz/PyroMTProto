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


class LoggedOut(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.LoggedOut`.

    Details:
        - Layer: ``227``
        - ID: ``C3A2835F``

    Parameters:
        future_auth_token (``bytes``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.LogOut
    """

    __slots__: list[str] = ["future_auth_token"]

    ID = 0xc3a2835f
    QUALNAME = "types.auth.LoggedOut"

    def __init__(self, *, future_auth_token: Optional[bytes] = None) -> None:
        self.future_auth_token = future_auth_token  # flags.0?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoggedOut":
        
        flags = Int.read(b)
        
        future_auth_token = Bytes.read(b) if flags & (1 << 0) else None
        return LoggedOut(future_auth_token=future_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.future_auth_token is not None else 0
        b.write(Int(flags))
        
        if self.future_auth_token is not None:
            b.write(Bytes(self.future_auth_token))
        
        return b.getvalue()
