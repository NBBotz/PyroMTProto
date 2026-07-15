#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .answer_callback_query import AnswerCallbackQuery
from .answer_inline_query import AnswerInlineQuery
from .answer_web_app_query import AnswerWebAppQuery
from .delete_bot_commands import DeleteBotCommands
from .get_bot_commands import GetBotCommands
from .get_bot_default_privileges import GetBotDefaultPrivileges
from .get_bot_info_description import GetBotInfoDescription
from .get_bot_info_short_description import GetBotInfoShortDescription
from .get_bot_name import GetBotName
from .get_chat_menu_button import GetChatMenuButton
from .get_game_high_scores import GetGameHighScores
from .get_inline_bot_results import GetInlineBotResults
from .request_callback_answer import RequestCallbackAnswer
from .send_game import SendGame
from .send_message_draft import SendMessageDraft
from .send_inline_bot_result import SendInlineBotResult
from .send_web_app_custom_request import SendWebAppCustomRequest
from .set_bot_commands import SetBotCommands
from .set_bot_default_privileges import SetBotDefaultPrivileges
from .set_bot_info_description import SetBotInfoDescription
from .set_bot_info_short_description import SetBotInfoShortDescription
from .set_bot_name import SetBotName
from .set_chat_menu_button import SetChatMenuButton
from .set_game_score import SetGameScore
from .get_owned_bots import GetOwnedBots
from .get_similar_bots import GetSimilarBots


class Bots(
    AnswerCallbackQuery,
    AnswerInlineQuery,
    AnswerWebAppQuery,
    SendWebAppCustomRequest,
    GetInlineBotResults,
    RequestCallbackAnswer,
    SendInlineBotResult,
    SendGame,
    SetGameScore,
    GetGameHighScores,
    SetBotCommands,
    GetBotCommands,
    DeleteBotCommands,
    SetBotDefaultPrivileges,
    GetBotDefaultPrivileges,
    SetChatMenuButton,
    GetChatMenuButton,
    SetBotInfoDescription,
    GetBotInfoDescription,
    SetBotInfoShortDescription,
    GetBotInfoShortDescription,
    SetBotName,
    GetBotName,
    GetOwnedBots,
    GetSimilarBots,
    SendMessageDraft,
):
    pass
