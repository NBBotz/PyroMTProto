#  PyroMTProto - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present PyroMTProto Contributors
#  Licensed under the GNU Lesser General Public License v3.0

from typing import Optional, Union
import pyrogram
from pyrogram import raw, enums


class UpdateBusinessAwayMessage:
    async def update_business_away_message(
        self: "pyrogram.Client",
        shortcut_id: Optional[int] = None,
        schedule: str = "always",
        recipients_type: str = "all",
        recipients: Optional[list] = None,
        exclude_recipients: Optional[list] = None,
        offline_only: bool = False,
    ) -> bool:
        """Set or clear your Business away message.

        The away message is sent automatically when you are unavailable.

        Parameters:
            shortcut_id (``int``, *optional*):
                ID of the quick-reply shortcut whose messages will be sent
                as the away response. Pass None to disable away messages.

            schedule (``str``, *optional*):
                When to send the away message. One of:
                - ``"always"`` — always send (default)
                - ``"outside_work_hours"`` — only outside working hours
                - ``"custom"`` — use custom_period (not yet exposed; contact Telegram)

            recipients_type (``str``, *optional*):
                Who receives the away message:
                - ``"all"`` — everyone (default)
                - ``"contacts"`` — contacts only
                - ``"non_contacts"`` — non-contacts only
                - ``"selected"`` — users in ``recipients``

            recipients (``list`` of ``int``, *optional*):
                User IDs to include when ``recipients_type="selected"``.

            exclude_recipients (``list`` of ``int``, *optional*):
                User IDs to exclude (when ``recipients_type="all"``).

            offline_only (``bool``, *optional*):
                Only send away message when you are offline. Defaults to False.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Away message for everyone when offline
                await app.update_business_away_message(
                    shortcut_id=1,
                    offline_only=True
                )

                # Away message only outside work hours for non-contacts
                await app.update_business_away_message(
                    shortcut_id=1,
                    schedule="outside_work_hours",
                    recipients_type="non_contacts"
                )

                # Disable away message
                await app.update_business_away_message()
        """
        away_message = None
        if shortcut_id is not None:
            # Build schedule
            if schedule == "outside_work_hours":
                sched = raw.types.BusinessAwayMessageScheduleOutsideWorkHours()
            else:
                sched = raw.types.BusinessAwayMessageScheduleAlways()

            # Build recipients
            if recipients_type == "contacts":
                rcpts = raw.types.BusinessRecipients(contacts=True)
            elif recipients_type == "non_contacts":
                rcpts = raw.types.BusinessRecipients(non_contacts=True)
            elif recipients_type == "selected" and recipients:
                rcpts = raw.types.BusinessRecipients(
                    users=[raw.types.InputUser(user_id=uid, access_hash=0) for uid in recipients],
                )
            else:
                # "all" — exclude specified users if any
                rcpts = raw.types.BusinessRecipients(
                    all_users=True,
                    exclude_users=[
                        raw.types.InputUser(user_id=uid, access_hash=0)
                        for uid in (exclude_recipients or [])
                    ] or None,
                )

            away_message = raw.types.BusinessAwayMessage(
                shortcut_id=shortcut_id,
                schedule=sched,
                recipients=rcpts,
                offline_only=offline_only,
            )

        await self.invoke(
            raw.functions.account.UpdateBusinessAwayMessage(away_message=away_message)
        )
        return True
