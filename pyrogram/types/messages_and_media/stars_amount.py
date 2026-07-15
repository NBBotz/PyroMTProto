#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from ..object import Object


class StarsAmount(Object):
    """Represents a Telegram Stars amount with optional nanos.

    Parameters:
        amount (``int``):
            Whole number of Stars.

        nanos (``int``):
            Fractional Stars in nano units (amount * 10^9).
    """

    def __init__(self, *, amount: int, nanos: int = 0):
        super().__init__()
        self.amount = amount
        self.nanos = nanos

    @staticmethod
    def _parse(stars) -> "StarsAmount | None":
        if stars is None:
            return None
        return StarsAmount(
            amount=getattr(stars, "amount", 0),
            nanos=getattr(stars, "nanos", 0),
        )

    def write(self):
        from pyrogram import raw
        return raw.types.StarsAmount(amount=self.amount, nanos=self.nanos)
