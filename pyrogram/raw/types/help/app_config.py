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


class AppConfig(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.AppConfig`.

    Details:
        - Layer: ``227``
        - ID: ``DD18782E``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        config (:obj:`JSONValue <pyrogram.raw.base.JSONValue>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppConfig
    """

    __slots__: list[str] = ["hash", "config"]

    ID = 0xdd18782e
    QUALNAME = "types.help.AppConfig"

    def __init__(self, *, hash: int, config: "raw.base.JSONValue") -> None:
        self.hash = hash  # int
        self.config = config  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppConfig":
        # No flags
        
        hash = Int.read(b)
        
        config = TLObject.read(b)
        
        return AppConfig(hash=hash, config=config)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(self.config.write())
        
        return b.getvalue()
