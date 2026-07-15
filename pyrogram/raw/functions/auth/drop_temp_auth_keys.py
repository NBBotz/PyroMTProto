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


class DropTempAuthKeys(TLObject["raw.base.Bool"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``8E48A188``

    Parameters:
        except_auth_keys (List of ``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["except_auth_keys"]

    ID = 0x8e48a188
    QUALNAME = "functions.auth.DropTempAuthKeys"

    def __init__(self, *, except_auth_keys: list[int]) -> None:
        self.except_auth_keys = except_auth_keys  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DropTempAuthKeys":
        # No flags
        
        except_auth_keys = TLObject.read(b, Long)
        
        return DropTempAuthKeys(except_auth_keys=except_auth_keys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.except_auth_keys, Long))
        
        return b.getvalue()
