#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .load_group_call_participants import LoadGroupCallParticipants
from .invite_group_call_participants import InviteGroupCallParticipants
from .create_video_chat import CreateVideoChat
from .discard_group_call import DiscardGroupCall
from .get_video_chat_rtmp_url import GetVideoChatRtmpUrl


class Phone(
    InviteGroupCallParticipants,
    LoadGroupCallParticipants,
    CreateVideoChat,
    DiscardGroupCall,
    GetVideoChatRtmpUrl,
):
    pass
