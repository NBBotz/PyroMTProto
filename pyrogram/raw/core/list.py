#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Any

from .tl_object import TLObject


class List(list[Any], TLObject):
    def __repr__(self) -> str:
        return f"pyrogram.raw.core.List([{','.join(TLObject.__repr__(i) for i in self)}])"
