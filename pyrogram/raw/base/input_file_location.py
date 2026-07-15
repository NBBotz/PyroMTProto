#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    InputFileLocation = Union[raw.types.InputDocumentFileLocation, raw.types.InputEncryptedFileLocation, raw.types.InputFileLocation, raw.types.InputGroupCallStream, raw.types.InputPeerPhotoFileLocation, raw.types.InputPeerPhotoFileLocationLegacy, raw.types.InputPhotoFileLocation, raw.types.InputPhotoLegacyFileLocation, raw.types.InputSecureFileLocation, raw.types.InputStickerSetThumb, raw.types.InputStickerSetThumbLegacy, raw.types.InputTakeoutFileLocation]
else:
    # noinspection PyRedeclaration
    class InputFileLocation(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 12 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputDocumentFileLocation
            InputEncryptedFileLocation
            InputFileLocation
            InputGroupCallStream
            InputPeerPhotoFileLocation
            InputPeerPhotoFileLocationLegacy
            InputPhotoFileLocation
            InputPhotoLegacyFileLocation
            InputSecureFileLocation
            InputStickerSetThumb
            InputStickerSetThumbLegacy
            InputTakeoutFileLocation
        """

        QUALNAME = "pyrogram.raw.base.InputFileLocation"
        __union_types__ = Union[raw.types.InputDocumentFileLocation, raw.types.InputEncryptedFileLocation, raw.types.InputFileLocation, raw.types.InputGroupCallStream, raw.types.InputPeerPhotoFileLocation, raw.types.InputPeerPhotoFileLocationLegacy, raw.types.InputPhotoFileLocation, raw.types.InputPhotoLegacyFileLocation, raw.types.InputSecureFileLocation, raw.types.InputStickerSetThumb, raw.types.InputStickerSetThumbLegacy, raw.types.InputTakeoutFileLocation]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/input-file-location"
            )
