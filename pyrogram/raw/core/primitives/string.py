#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from io import BytesIO
from typing import cast

from .bytes import Bytes


class String(Bytes):
    @classmethod
    def read(cls, data: BytesIO, *args) -> str:  # type: ignore
        return cast(bytes, super(String, String).read(data)).decode(errors="replace")

    def __new__(cls, value: str) -> bytes:  # type: ignore
        return super().__new__(cls, value.encode())
