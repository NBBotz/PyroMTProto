#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .activate_stealth_mode import ActivateStealthMode
from .can_post_story import CanPostStory
from .copy_story import CopyStory
from .delete_stories import DeleteStories
from .edit_story import EditStory
from .export_story_link import ExportStoryLink
from .forward_story import ForwardStory
from .get_all_stories import GetAllStories
from .get_chat_active_stories import GetChatActiveStories
from .get_chat_archived_stories import GetChatArchivedStories
from .get_pinned_stories import GetPinnedStories
from .get_stories import GetStories
from .get_story_reactions import GetStoryReactions
from .get_story_viewers import GetStoryViewers
from .hide_chat_stories import HideChatStories
from .hide_my_story_view import HideMyStoryView
from .increment_story_views import IncrementStoryViews
from .pin_chat_stories import PinChatStories
from .post_story import PostStory
from .read_chat_stories import ReadChatStories
from .send_story_reaction import SendStoryReaction
from .show_chat_stories import ShowChatStories
from .toggle_story_is_posted_to_chat_page import ToggleStoryIsPostedToChatPage
from .unpin_chat_stories import UnpinChatStories


class Stories(
    ActivateStealthMode,
    CanPostStory,
    CopyStory,
    DeleteStories,
    EditStory,
    ExportStoryLink,
    ForwardStory,
    GetAllStories,
    GetChatActiveStories,
    GetChatArchivedStories,
    GetPinnedStories,
    GetStories,
    GetStoryReactions,
    GetStoryViewers,
    HideChatStories,
    HideMyStoryView,
    IncrementStoryViews,
    PinChatStories,
    PostStory,
    ReadChatStories,
    SendStoryReaction,
    ShowChatStories,
    ToggleStoryIsPostedToChatPage,
    UnpinChatStories,
):
    pass
