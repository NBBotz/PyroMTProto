#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .get_privacy import GetPrivacy
from .set_privacy import SetPrivacy
from .get_global_privacy_settings import GetGlobalPrivacySettings
from .set_global_privacy_settings import SetGlobalPrivacySettings
from .get_account_ttl import GetAccountTtl
from .set_account_ttl import SetAccountTtl
from .set_inactive_session_ttl import SetInactiveSessionTtl
from .add_profile_audio import AddProfileAudio
from .remove_profile_audio import RemoveProfileAudio
from .set_profile_audio_position import SetProfileAudioPosition


class Account(
    GetPrivacy,
    SetPrivacy,
    GetGlobalPrivacySettings,
    SetGlobalPrivacySettings,
    GetAccountTtl,
    SetAccountTtl,
    SetInactiveSessionTtl,
    AddProfileAudio,
    RemoveProfileAudio,
    SetProfileAudioPosition,
):
    pass
