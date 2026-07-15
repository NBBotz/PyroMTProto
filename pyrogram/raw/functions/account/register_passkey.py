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


class RegisterPasskey(TLObject["raw.base.Passkey"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``55B41FD6``

    Parameters:
        credential (:obj:`InputPasskeyCredential <pyrogram.raw.base.InputPasskeyCredential>`):
            N/A

    Returns:
        :obj:`Passkey <pyrogram.raw.base.Passkey>`
    """

    __slots__: list[str] = ["credential"]

    ID = 0x55b41fd6
    QUALNAME = "functions.account.RegisterPasskey"

    def __init__(self, *, credential: "raw.base.InputPasskeyCredential") -> None:
        self.credential = credential  # InputPasskeyCredential

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RegisterPasskey":
        # No flags
        
        credential = TLObject.read(b)
        
        return RegisterPasskey(credential=credential)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.credential.write())
        
        return b.getvalue()
