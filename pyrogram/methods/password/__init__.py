#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .change_cloud_password import ChangeCloudPassword
from .enable_cloud_password import EnableCloudPassword
from .remove_cloud_password import RemoveCloudPassword


class Password(
    ChangeCloudPassword,
    EnableCloudPassword,
    RemoveCloudPassword,
):
    pass
