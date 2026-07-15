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


class PreviewInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.bots.PreviewInfo`.

    Details:
        - Layer: ``227``
        - ID: ``CA71D64``

    Parameters:
        media (List of :obj:`BotPreviewMedia <pyrogram.raw.base.BotPreviewMedia>`):
            N/A

        lang_codes (List of ``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetPreviewInfo
    """

    __slots__: list[str] = ["media", "lang_codes"]

    ID = 0xca71d64
    QUALNAME = "types.bots.PreviewInfo"

    def __init__(self, *, media: list["raw.base.BotPreviewMedia"], lang_codes: list[str]) -> None:
        self.media = media  # Vector<BotPreviewMedia>
        self.lang_codes = lang_codes  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PreviewInfo":
        # No flags
        
        media = TLObject.read(b)
        
        lang_codes = TLObject.read(b, String)
        
        return PreviewInfo(media=media, lang_codes=lang_codes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.media))
        
        b.write(Vector(self.lang_codes, String))
        
        return b.getvalue()
