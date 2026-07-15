#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Union

import pyrogram
from pyrogram import raw

from .story_privacy_settings import StoryPrivacySettings


class StoryPrivacySettingsEveryone(StoryPrivacySettings):
    """The story can be viewed by everyone.

    Parameters:
        except_user_ids (List of ``int`` | ``str``, *optional*):
            Identifiers of the users that can't see the story; always unknown and empty for non-owned stories.

    """

    def __init__(self, *, except_user_ids: list[Union[int, str]]=None):
        super().__init__()

        self.except_user_ids = except_user_ids

    async def write(self, client: "pyrogram.Client"):
        privacy_rules = []
        privacy_rules.append(raw.types.InputPrivacyValueAllowAll())
        users = [await client.resolve_peer(user_id) for user_id in (self.except_user_ids or [])]
        if users:
            privacy_rules.append(raw.types.InputPrivacyValueDisallowUsers(users=users))
        return privacy_rules
