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


class DataJSON(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DataJSON`.

    Details:
        - Layer: ``227``
        - ID: ``7D748D04``

    Parameters:
        data (``str``):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.SendCustomRequest
            bots.InvokeWebViewCustomMethod
            phone.GetCallConfig
    """

    __slots__: list[str] = ["data"]

    ID = 0x7d748d04
    QUALNAME = "types.DataJSON"

    def __init__(self, *, data: str) -> None:
        self.data = data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DataJSON":
        # No flags
        
        data = String.read(b)
        
        return DataJSON(data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.data))
        
        return b.getvalue()
