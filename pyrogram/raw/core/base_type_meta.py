#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import get_args

class BaseTypeMeta(type):
    def __instancecheck__(cls, instance):
        return isinstance(instance, get_args(cls.__union_types__))

    def __subclasscheck__(cls, subclass):
        return issubclass(subclass, get_args(cls.__union_types__))
