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


class WebBrowserSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.WebBrowserSettings`.

    Details:
        - Layer: ``227``
        - ID: ``79EB8CB3``

    Parameters:
        external_exceptions (List of :obj:`WebDomainException <pyrogram.raw.base.WebDomainException>`):
            N/A

        inapp_exceptions (List of :obj:`WebDomainException <pyrogram.raw.base.WebDomainException>`):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        open_external_browser (``bool``, *optional*):
            N/A

        display_close_button (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWebBrowserSettings
            account.UpdateWebBrowserSettings
            account.DeleteWebBrowserSettingsExceptions
    """

    __slots__: list[str] = ["external_exceptions", "inapp_exceptions", "hash", "open_external_browser", "display_close_button"]

    ID = 0x79eb8cb3
    QUALNAME = "types.account.WebBrowserSettings"

    def __init__(self, *, external_exceptions: list["raw.base.WebDomainException"], inapp_exceptions: list["raw.base.WebDomainException"], hash: int, open_external_browser: Optional[bool] = None, display_close_button: Optional[bool] = None) -> None:
        self.external_exceptions = external_exceptions  # Vector<WebDomainException>
        self.inapp_exceptions = inapp_exceptions  # Vector<WebDomainException>
        self.hash = hash  # long
        self.open_external_browser = open_external_browser  # flags.0?true
        self.display_close_button = display_close_button  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebBrowserSettings":
        
        flags = Int.read(b)
        
        open_external_browser = True if flags & (1 << 0) else False
        display_close_button = True if flags & (1 << 1) else False
        external_exceptions = TLObject.read(b)
        
        inapp_exceptions = TLObject.read(b)
        
        hash = Long.read(b)
        
        return WebBrowserSettings(external_exceptions=external_exceptions, inapp_exceptions=inapp_exceptions, hash=hash, open_external_browser=open_external_browser, display_close_button=display_close_button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open_external_browser else 0
        flags |= (1 << 1) if self.display_close_button else 0
        b.write(Int(flags))
        
        b.write(Vector(self.external_exceptions))
        
        b.write(Vector(self.inapp_exceptions))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
