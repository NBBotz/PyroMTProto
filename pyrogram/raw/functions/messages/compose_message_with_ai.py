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


class ComposeMessageWithAI(TLObject["raw.base.messages.ComposedMessageWithAI"]):
    """Telegram API function.

    Details:
        - Layer: ``227``
        - ID: ``DAECC589``

    Parameters:
        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        proofread (``bool``, *optional*):
            N/A

        emojify (``bool``, *optional*):
            N/A

        translate_to_lang (``str``, *optional*):
            N/A

        tone (:obj:`InputAiComposeTone <pyrogram.raw.base.InputAiComposeTone>`, *optional*):
            N/A

    Returns:
        :obj:`messages.ComposedMessageWithAI <pyrogram.raw.base.messages.ComposedMessageWithAI>`
    """

    __slots__: list[str] = ["text", "proofread", "emojify", "translate_to_lang", "tone"]

    ID = 0xdaecc589
    QUALNAME = "functions.messages.ComposeMessageWithAI"

    def __init__(self, *, text: "raw.base.TextWithEntities", proofread: Optional[bool] = None, emojify: Optional[bool] = None, translate_to_lang: Optional[str] = None, tone: "raw.base.InputAiComposeTone" = None) -> None:
        self.text = text  # TextWithEntities
        self.proofread = proofread  # flags.0?true
        self.emojify = emojify  # flags.3?true
        self.translate_to_lang = translate_to_lang  # flags.1?string
        self.tone = tone  # flags.2?InputAiComposeTone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ComposeMessageWithAI":
        
        flags = Int.read(b)
        
        proofread = True if flags & (1 << 0) else False
        emojify = True if flags & (1 << 3) else False
        text = TLObject.read(b)
        
        translate_to_lang = String.read(b) if flags & (1 << 1) else None
        tone = TLObject.read(b) if flags & (1 << 2) else None
        
        return ComposeMessageWithAI(text=text, proofread=proofread, emojify=emojify, translate_to_lang=translate_to_lang, tone=tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.proofread else 0
        flags |= (1 << 3) if self.emojify else 0
        flags |= (1 << 1) if self.translate_to_lang is not None else 0
        flags |= (1 << 2) if self.tone is not None else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        if self.translate_to_lang is not None:
            b.write(String(self.translate_to_lang))
        
        if self.tone is not None:
            b.write(self.tone.write())
        
        return b.getvalue()
