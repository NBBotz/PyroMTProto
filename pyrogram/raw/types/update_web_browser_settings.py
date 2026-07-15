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


class UpdateWebBrowserSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``C39A2ADE``

    Parameters:
        open_external_browser (``bool``, *optional*):
            N/A

        display_close_button (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["open_external_browser", "display_close_button"]

    ID = 0xc39a2ade
    QUALNAME = "types.UpdateWebBrowserSettings"

    def __init__(self, *, open_external_browser: Optional[bool] = None, display_close_button: Optional[bool] = None) -> None:
        self.open_external_browser = open_external_browser  # flags.0?true
        self.display_close_button = display_close_button  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebBrowserSettings":
        
        flags = Int.read(b)
        
        open_external_browser = True if flags & (1 << 0) else False
        display_close_button = True if flags & (1 << 1) else False
        return UpdateWebBrowserSettings(open_external_browser=open_external_browser, display_close_button=display_close_button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open_external_browser else 0
        flags |= (1 << 1) if self.display_close_button else 0
        b.write(Int(flags))
        
        return b.getvalue()
