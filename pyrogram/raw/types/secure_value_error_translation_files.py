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


class SecureValueErrorTranslationFiles(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``227``
        - ID: ``34636DD8``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

        file_hash (List of ``bytes``):
            N/A

        text (``str``):
            N/A

    """

    __slots__: list[str] = ["type", "file_hash", "text"]

    ID = 0x34636dd8
    QUALNAME = "types.SecureValueErrorTranslationFiles"

    def __init__(self, *, type: "raw.base.SecureValueType", file_hash: list[bytes], text: str) -> None:
        self.type = type  # SecureValueType
        self.file_hash = file_hash  # Vector<bytes>
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorTranslationFiles":
        # No flags
        
        type = TLObject.read(b)
        
        file_hash = TLObject.read(b, Bytes)
        
        text = String.read(b)
        
        return SecureValueErrorTranslationFiles(type=type, file_hash=file_hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Vector(self.file_hash, Bytes))
        
        b.write(String(self.text))
        
        return b.getvalue()
