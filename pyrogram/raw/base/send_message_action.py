#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import TYPE_CHECKING, Union
from pyrogram import raw
from pyrogram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    SendMessageAction = Union[raw.types.InputSendMessageRichMessageDraftAction, raw.types.SendMessageCancelAction, raw.types.SendMessageChooseContactAction, raw.types.SendMessageChooseStickerAction, raw.types.SendMessageEmojiInteraction, raw.types.SendMessageEmojiInteractionSeen, raw.types.SendMessageGamePlayAction, raw.types.SendMessageGeoLocationAction, raw.types.SendMessageHistoryImportAction, raw.types.SendMessageRecordAudioAction, raw.types.SendMessageRecordRoundAction, raw.types.SendMessageRecordVideoAction, raw.types.SendMessageRichMessageDraftAction, raw.types.SendMessageTextDraftAction, raw.types.SendMessageTypingAction, raw.types.SendMessageUploadAudioAction, raw.types.SendMessageUploadDocumentAction, raw.types.SendMessageUploadPhotoAction, raw.types.SendMessageUploadRoundAction, raw.types.SendMessageUploadVideoAction, raw.types.SpeakingInGroupCallAction]
else:
    # noinspection PyRedeclaration
    class SendMessageAction(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 21 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputSendMessageRichMessageDraftAction
            SendMessageCancelAction
            SendMessageChooseContactAction
            SendMessageChooseStickerAction
            SendMessageEmojiInteraction
            SendMessageEmojiInteractionSeen
            SendMessageGamePlayAction
            SendMessageGeoLocationAction
            SendMessageHistoryImportAction
            SendMessageRecordAudioAction
            SendMessageRecordRoundAction
            SendMessageRecordVideoAction
            SendMessageRichMessageDraftAction
            SendMessageTextDraftAction
            SendMessageTypingAction
            SendMessageUploadAudioAction
            SendMessageUploadDocumentAction
            SendMessageUploadPhotoAction
            SendMessageUploadRoundAction
            SendMessageUploadVideoAction
            SpeakingInGroupCallAction
        """

        QUALNAME = "pyrogram.raw.base.SendMessageAction"
        __union_types__ = Union[raw.types.InputSendMessageRichMessageDraftAction, raw.types.SendMessageCancelAction, raw.types.SendMessageChooseContactAction, raw.types.SendMessageChooseStickerAction, raw.types.SendMessageEmojiInteraction, raw.types.SendMessageEmojiInteractionSeen, raw.types.SendMessageGamePlayAction, raw.types.SendMessageGeoLocationAction, raw.types.SendMessageHistoryImportAction, raw.types.SendMessageRecordAudioAction, raw.types.SendMessageRecordRoundAction, raw.types.SendMessageRecordVideoAction, raw.types.SendMessageRichMessageDraftAction, raw.types.SendMessageTextDraftAction, raw.types.SendMessageTypingAction, raw.types.SendMessageUploadAudioAction, raw.types.SendMessageUploadDocumentAction, raw.types.SendMessageUploadPhotoAction, raw.types.SendMessageUploadRoundAction, raw.types.SendMessageUploadVideoAction, raw.types.SpeakingInGroupCallAction]

        def __init__(self):
            raise TypeError(
                "Base types can only be used for type checking purposes: "
                "you tried to use a base type instance as argument, "
                "but you need to instantiate one of its constructors instead. "
                "More info: https://telegramplayground.github.io/pyrogram/telegram/base/send-message-action"
            )
