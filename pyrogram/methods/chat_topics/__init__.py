#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .get_forum_topic_icon_stickers import GetForumTopicIconStickers
from .create_forum_topic import CreateForumTopic
from .edit_forum_topic import EditForumTopic
from .close_forum_topic import CloseForumTopic
from .reopen_forum_topic import ReopenForumTopic
from .hide_forum_topic import HideForumTopic
from .unhide_forum_topic import UnhideForumTopic
from .delete_forum_topic import DeleteForumTopic
from .get_forum_topics import GetForumTopics
from .get_forum_topic import GetForumTopic
from .toggle_forum_topic_is_pinned import ToggleForumTopicIsPinned


class ChatTopics(
    CloseForumTopic,
    CreateForumTopic,
    DeleteForumTopic,
    EditForumTopic,
    GetForumTopic,
    GetForumTopicIconStickers,
    GetForumTopics,
    HideForumTopic,
    ReopenForumTopic,
    UnhideForumTopic,
    ToggleForumTopicIsPinned,
):
    pass
