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


class RequestedButton(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.bots.RequestedButton`.

    Details:
        - Layer: ``227``
        - ID: ``F13BBCD7``

    Parameters:
        webapp_req_id (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.RequestWebViewButton
    """

    __slots__: list[str] = ["webapp_req_id"]

    ID = 0xf13bbcd7
    QUALNAME = "types.bots.RequestedButton"

    def __init__(self, *, webapp_req_id: str) -> None:
        self.webapp_req_id = webapp_req_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedButton":
        # No flags
        
        webapp_req_id = String.read(b)
        
        return RequestedButton(webapp_req_id=webapp_req_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.webapp_req_id))
        
        return b.getvalue()
