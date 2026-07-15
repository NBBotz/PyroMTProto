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


class TranslateText(TLObject["raw.base.messages.TranslatedText"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``A5EEC345``

    Parameters:
        to_lang (``str``):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        id (List of ``int`` ``32-bit``, *optional*):
            N/A

        text (List of :obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

        tone (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.TranslatedText <pyrogram.raw.base.messages.TranslatedText>`
    """

    __slots__: list[str] = ["to_lang", "peer", "id", "text", "tone"]

    ID = 0xa5eec345
    QUALNAME = "functions.messages.TranslateText"

    def __init__(self, *, to_lang: str, peer: "raw.base.InputPeer" = None, id: Optional[list[int]] = None, text: Optional[list["raw.base.TextWithEntities"]] = None, tone: Optional[str] = None) -> None:
        self.to_lang = to_lang  # string
        self.peer = peer  # flags.0?InputPeer
        self.id = id  # flags.0?Vector<int>
        self.text = text  # flags.1?Vector<TextWithEntities>
        self.tone = tone  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranslateText":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 0) else None
        
        id = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        text = TLObject.read(b) if flags & (1 << 1) else []
        
        to_lang = String.read(b)
        
        tone = String.read(b) if flags & (1 << 2) else None
        return TranslateText(to_lang=to_lang, peer=peer, id=id, text=text, tone=tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.peer is not None else 0
        flags |= (1 << 0) if self.id else 0
        flags |= (1 << 1) if self.text else 0
        flags |= (1 << 2) if self.tone is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.id is not None:
            b.write(Vector(self.id, Int))
        
        if self.text is not None:
            b.write(Vector(self.text))
        
        b.write(String(self.to_lang))
        
        if self.tone is not None:
            b.write(String(self.tone))
        
        return b.getvalue()
