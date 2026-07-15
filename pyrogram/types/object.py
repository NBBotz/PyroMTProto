#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

import re
from datetime import datetime
from enum import Enum
from json import dumps

import pyrogram


class Object:
    def __init__(self, client: "pyrogram.Client" = None):
        self._client = client

    def bind(self, client: "pyrogram.Client"):
        """Bind a Client instance to this and to all nested Pyrogram objects.

        Parameters:
            client (:obj:`~pyrogram.types.Client`):
                The Client instance to bind this object with. Useful to re-enable bound methods after serializing and
                deserializing Pyrogram objects with ``repr`` and ``eval``.
        """
        self._client = client

        for i in self.__dict__:
            o = getattr(self, i)

            if isinstance(o, Object):
                o.bind(client)

    @staticmethod
    def default(obj: "Object"):
        if hasattr(obj, "__custom__"):
            _custom_ = obj.__custom__()
            if _custom_ is not None:
                return _custom_

        if isinstance(obj, bytes):
            return repr(obj)

        if isinstance(obj, re.Match):
            return repr(obj)

        if isinstance(obj, Enum):
            return str(obj)

        if isinstance(obj, datetime):
            return str(obj)

        # TODO: #20
        if not hasattr(obj, "__dict__"):
            return obj.__class__.__name__

        return {
            "_": obj.__class__.__name__,
            **{
                attr: (
                    "*" * 9 if attr == "phone_number" else
                    getattr(obj, attr)
                )
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "pyrogram.types.{}({})".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            )
        )

    def __eq__(self, other: "Object") -> bool:
        for attr in self.__dict__:
            try:
                if attr.startswith("_"):
                    continue

                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __setstate__(self, state):
        for attr in state:
            obj = state[attr]

            # Maybe a better alternative would be https://docs.python.org/3/library/inspect.html#inspect.signature
            if isinstance(obj, tuple) and len(obj) == 2 and obj[0] == "dt":
                state[attr] = pyrogram.utils.timestamp_to_datetime(obj[1])

        self.__dict__ = state

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop("_client", None)

        for attr in state:
            obj = state[attr]

            if isinstance(obj, datetime):
                state[attr] = ("dt", obj.timestamp())

        return state
