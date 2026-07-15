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


class BotPreviewMedia(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotPreviewMedia`.

    Details:
        - Layer: ``227``
        - ID: ``23E91BA3``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.AddPreviewMedia
            bots.EditPreviewMedia
            bots.GetPreviewMedias
    """

    __slots__: list[str] = ["date", "media"]

    ID = 0x23e91ba3
    QUALNAME = "types.BotPreviewMedia"

    def __init__(self, *, date: int, media: "raw.base.MessageMedia") -> None:
        self.date = date  # int
        self.media = media  # MessageMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotPreviewMedia":
        # No flags
        
        date = Int.read(b)
        
        media = TLObject.read(b)
        
        return BotPreviewMedia(date=date, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(self.media.write())
        
        return b.getvalue()
