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


class InputPasskeyCredentialFirebasePNV(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPasskeyCredential`.

    Details:
        - Layer: ``227``
        - ID: ``5B1CCB28``

    Parameters:
        pnv_token (``str``):
            N/A

    """

    __slots__: list[str] = ["pnv_token"]

    ID = 0x5b1ccb28
    QUALNAME = "types.InputPasskeyCredentialFirebasePNV"

    def __init__(self, *, pnv_token: str) -> None:
        self.pnv_token = pnv_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPasskeyCredentialFirebasePNV":
        # No flags
        
        pnv_token = String.read(b)
        
        return InputPasskeyCredentialFirebasePNV(pnv_token=pnv_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.pnv_token))
        
        return b.getvalue()
