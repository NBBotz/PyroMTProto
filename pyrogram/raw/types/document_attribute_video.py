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


class DocumentAttributeVideo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``227``
        - ID: ``43C57C48``

    Parameters:
        duration (``float`` ``64-bit``):
            N/A

        w (``int`` ``32-bit``):
            N/A

        h (``int`` ``32-bit``):
            N/A

        round_message (``bool``, *optional*):
            N/A

        supports_streaming (``bool``, *optional*):
            N/A

        nosound (``bool``, *optional*):
            N/A

        preload_prefix_size (``int`` ``32-bit``, *optional*):
            N/A

        video_start_ts (``float`` ``64-bit``, *optional*):
            N/A

        video_codec (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["duration", "w", "h", "round_message", "supports_streaming", "nosound", "preload_prefix_size", "video_start_ts", "video_codec"]

    ID = 0x43c57c48
    QUALNAME = "types.DocumentAttributeVideo"

    def __init__(self, *, duration: float, w: int, h: int, round_message: Optional[bool] = None, supports_streaming: Optional[bool] = None, nosound: Optional[bool] = None, preload_prefix_size: Optional[int] = None, video_start_ts: Optional[float] = None, video_codec: Optional[str] = None) -> None:
        self.duration = duration  # double
        self.w = w  # int
        self.h = h  # int
        self.round_message = round_message  # flags.0?true
        self.supports_streaming = supports_streaming  # flags.1?true
        self.nosound = nosound  # flags.3?true
        self.preload_prefix_size = preload_prefix_size  # flags.2?int
        self.video_start_ts = video_start_ts  # flags.4?double
        self.video_codec = video_codec  # flags.5?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeVideo":
        
        flags = Int.read(b)
        
        round_message = True if flags & (1 << 0) else False
        supports_streaming = True if flags & (1 << 1) else False
        nosound = True if flags & (1 << 3) else False
        duration = Double.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        preload_prefix_size = Int.read(b) if flags & (1 << 2) else None
        video_start_ts = Double.read(b) if flags & (1 << 4) else None
        video_codec = String.read(b) if flags & (1 << 5) else None
        return DocumentAttributeVideo(duration=duration, w=w, h=h, round_message=round_message, supports_streaming=supports_streaming, nosound=nosound, preload_prefix_size=preload_prefix_size, video_start_ts=video_start_ts, video_codec=video_codec)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.round_message else 0
        flags |= (1 << 1) if self.supports_streaming else 0
        flags |= (1 << 3) if self.nosound else 0
        flags |= (1 << 2) if self.preload_prefix_size is not None else 0
        flags |= (1 << 4) if self.video_start_ts is not None else 0
        flags |= (1 << 5) if self.video_codec is not None else 0
        b.write(Int(flags))
        
        b.write(Double(self.duration))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        if self.preload_prefix_size is not None:
            b.write(Int(self.preload_prefix_size))
        
        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))
        
        if self.video_codec is not None:
            b.write(String(self.video_codec))
        
        return b.getvalue()
