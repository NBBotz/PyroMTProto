#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from .object import Object


class List(list):
    __slots__ = []

    def __str__(self):
        # noinspection PyCallByClass
        return Object.__str__(self)

    def __repr__(self):
        return f"pyrogram.types.List([{','.join(Object.__repr__(i) for i in self)}])"
