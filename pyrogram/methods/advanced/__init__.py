#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .invoke import Invoke
from .resolve_peer import ResolvePeer
from .save_file import SaveFile


class Advanced(
    Invoke,
    ResolvePeer,
    SaveFile
):
    pass
