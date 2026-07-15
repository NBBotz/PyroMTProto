#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .get_message_effects import GetMessageEffects
from .get_stickers import GetStickers


class Stickers(
    GetMessageEffects,
    GetStickers,
):
    pass
