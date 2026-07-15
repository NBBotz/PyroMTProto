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


class ToggleWebBrowserSettingsException(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``60ED4229``

    Parameters:
        url (``str``):
            N/A

        delete (``bool``, *optional*):
            N/A

        open_external_browser (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: list[str] = ["url", "delete", "open_external_browser"]

    ID = 0x60ed4229
    QUALNAME = "functions.account.ToggleWebBrowserSettingsException"

    def __init__(self, *, url: str, delete: Optional[bool] = None, open_external_browser: Optional[bool] = None) -> None:
        self.url = url  # string
        self.delete = delete  # flags.1?true
        self.open_external_browser = open_external_browser  # flags.0?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleWebBrowserSettingsException":
        
        flags = Int.read(b)
        
        delete = True if flags & (1 << 1) else False
        open_external_browser = Bool.read(b) if flags & (1 << 0) else None
        url = String.read(b)
        
        return ToggleWebBrowserSettingsException(url=url, delete=delete, open_external_browser=open_external_browser)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.delete else 0
        flags |= (1 << 0) if self.open_external_browser is not None else 0
        b.write(Int(flags))
        
        if self.open_external_browser is not None:
            b.write(Bool(self.open_external_browser))
        
        b.write(String(self.url))
        
        return b.getvalue()
