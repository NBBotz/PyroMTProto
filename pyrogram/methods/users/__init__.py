#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .block_user import BlockUser
from .delete_profile_photos import DeleteProfilePhotos
from .get_chat_photos import GetChatPhotos
from .get_chat_photos_count import GetChatPhotosCount
from .get_common_chats import GetCommonChats
from .get_default_emoji_statuses import GetDefaultEmojiStatuses
from .get_me import GetMe
from .get_users import GetUsers
from .set_emoji_status import SetEmojiStatus
from .set_profile_photo import SetProfilePhoto
from .set_username import SetUsername
from .unblock_user import UnblockUser
from .update_profile import UpdateProfile
from .set_birthdate import SetBirthdate
from .set_personal_chat import SetPersonalChat
from .update_status import UpdateStatus
from .delete_account import DeleteAccount


class Users(
    BlockUser,
    DeleteProfilePhotos,
    GetChatPhotos,
    GetChatPhotosCount,
    GetCommonChats,
    GetDefaultEmojiStatuses,
    GetMe,
    GetUsers,
    SetBirthdate,
    SetEmojiStatus,
    SetPersonalChat,
    SetProfilePhoto,
    SetUsername,
    UnblockUser,
    UpdateProfile,
    UpdateStatus,
    DeleteAccount,
):
    pass
