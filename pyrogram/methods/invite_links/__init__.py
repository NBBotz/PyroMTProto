#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .approve_all_chat_join_requests import ApproveAllChatJoinRequests
from .approve_chat_join_request import ApproveChatJoinRequest
from .create_chat_invite_link import CreateChatInviteLink
from .decline_all_chat_join_requests import DeclineAllChatJoinRequests
from .decline_chat_join_request import DeclineChatJoinRequest
from .delete_chat_admin_invite_links import DeleteChatAdminInviteLinks
from .delete_chat_invite_link import DeleteChatInviteLink
from .edit_chat_invite_link import EditChatInviteLink
from .export_chat_invite_link import ExportChatInviteLink
from .get_chat_admin_invite_links import GetChatAdminInviteLinks
from .get_chat_admin_invite_links_count import GetChatAdminInviteLinksCount
from .get_chat_admins_with_invite_links import GetChatAdminsWithInviteLinks
from .get_chat_invite_link import GetChatInviteLink
from .get_chat_invite_link_joiners import GetChatInviteLinkJoiners
from .get_chat_invite_link_joiners_count import GetChatInviteLinkJoinersCount
from .get_chat_join_requests import GetChatJoinRequests
from .revoke_chat_invite_link import RevokeChatInviteLink


class InviteLinks(
    ApproveAllChatJoinRequests,
    ApproveChatJoinRequest,
    CreateChatInviteLink,
    DeclineAllChatJoinRequests,
    DeclineChatJoinRequest,
    DeleteChatAdminInviteLinks,
    DeleteChatInviteLink,
    EditChatInviteLink,
    ExportChatInviteLink,
    GetChatAdminInviteLinks,
    GetChatAdminInviteLinksCount,
    GetChatAdminsWithInviteLinks,
    GetChatInviteLink,
    GetChatInviteLinkJoiners,
    GetChatInviteLinkJoinersCount,
    GetChatJoinRequests,
    RevokeChatInviteLink,
):
    pass
