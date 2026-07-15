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


class UpdateWebBrowserException(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``227``
        - ID: ``140502D1``

    Parameters:
        exception (:obj:`WebDomainException <pyrogram.raw.base.WebDomainException>`):
            N/A

        delete (``bool``, *optional*):
            N/A

        open_external_browser (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["exception", "delete", "open_external_browser"]

    ID = 0x140502d1
    QUALNAME = "types.UpdateWebBrowserException"

    def __init__(self, *, exception: "raw.base.WebDomainException", delete: Optional[bool] = None, open_external_browser: Optional[bool] = None) -> None:
        self.exception = exception  # WebDomainException
        self.delete = delete  # flags.1?true
        self.open_external_browser = open_external_browser  # flags.0?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebBrowserException":
        
        flags = Int.read(b)
        
        delete = True if flags & (1 << 1) else False
        open_external_browser = Bool.read(b) if flags & (1 << 0) else None
        exception = TLObject.read(b)
        
        return UpdateWebBrowserException(exception=exception, delete=delete, open_external_browser=open_external_browser)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.delete else 0
        flags |= (1 << 0) if self.open_external_browser is not None else 0
        b.write(Int(flags))
        
        if self.open_external_browser is not None:
            b.write(Bool(self.open_external_browser))
        
        b.write(self.exception.write())
        
        return b.getvalue()
