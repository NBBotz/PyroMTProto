#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from datetime import datetime
from typing import Optional, TYPE_CHECKING

from ..object import Object

if TYPE_CHECKING:
    pass


class SuggestedPost(Object):
    """Describes the suggested-post status attached to a message.

    When a user sends a suggested post to a channel (where the user is
    not an admin), the message carries a :obj:`SuggestedPost` object
    containing its current approval status and optional scheduling info.

    Parameters:
        accepted (``bool``):\n
            True if the suggested post was approved by the channel admin.

        rejected (``bool``):
            True if the suggested post was rejected.

        price (``object``, *optional*):
            Stars amount that the channel will pay to the post author
            upon approval (if any).

        schedule_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the post is scheduled to be published (if set).
    """

    def __init__(
        self,
        *,
        accepted: bool = False,
        rejected: bool = False,
        price=None,
        schedule_date: Optional[datetime] = None
    ):
        super().__init__()
        self.accepted = accepted
        self.rejected = rejected
        self.price = price
        self.schedule_date = schedule_date

    @property
    def is_pending(self) -> bool:
        """True if the post is still waiting for a decision."""
        return not self.accepted and not self.rejected

    @property
    def is_scheduled(self) -> bool:
        """True if the post has a scheduled publish date."""
        return self.schedule_date is not None
