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


class Passkeys(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.Passkeys`.

    Details:
        - Layer: ``227``
        - ID: ``F8E0AA1C``

    Parameters:
        passkeys (List of :obj:`Passkey <pyrogram.raw.base.Passkey>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPasskeys
    """

    __slots__: list[str] = ["passkeys"]

    ID = 0xf8e0aa1c
    QUALNAME = "types.account.Passkeys"

    def __init__(self, *, passkeys: list["raw.base.Passkey"]) -> None:
        self.passkeys = passkeys  # Vector<Passkey>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Passkeys":
        # No flags
        
        passkeys = TLObject.read(b)
        
        return Passkeys(passkeys=passkeys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.passkeys))
        
        return b.getvalue()
