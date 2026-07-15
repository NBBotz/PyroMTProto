#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .get_boost_status import GetBoostStatus
from .get_boosts_list import GetBoostsList
from .apply_boost import ApplyBoost
from .get_my_boosts import GetMyBoosts
from .get_user_boosts import GetUserBoosts


class Premium(
    GetBoostStatus,
    GetBoostsList,
    ApplyBoost,
    GetMyBoosts,
    GetUserBoosts,
):
    pass
