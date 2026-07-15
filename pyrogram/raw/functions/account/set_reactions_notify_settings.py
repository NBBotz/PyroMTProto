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


class SetReactionsNotifySettings(TLObject["raw.base.ReactionsNotifySettings"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``316CE548``

    Parameters:
        settings (:obj:`ReactionsNotifySettings <pyrogram.raw.base.ReactionsNotifySettings>`):
            N/A

    Returns:
        :obj:`ReactionsNotifySettings <pyrogram.raw.base.ReactionsNotifySettings>`
    """

    __slots__: list[str] = ["settings"]

    ID = 0x316ce548
    QUALNAME = "functions.account.SetReactionsNotifySettings"

    def __init__(self, *, settings: "raw.base.ReactionsNotifySettings") -> None:
        self.settings = settings  # ReactionsNotifySettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetReactionsNotifySettings":
        # No flags
        
        settings = TLObject.read(b)
        
        return SetReactionsNotifySettings(settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.settings.write())
        
        return b.getvalue()
